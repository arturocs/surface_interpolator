use actix_web::{get, web, App, HttpServer, Responder};
use async_once::AsyncOnce;
use futures::TryStreamExt;
use lazy_static::lazy_static;
use mongodb::{bson::doc, Client, Collection};
use serde::{Deserialize, Serialize};

lazy_static! {
    static ref BOOKS: AsyncOnce<Collection<Book>> = AsyncOnce::new(async {
        let client = Client::with_uri_str("mongodb://mongo:27017").await.unwrap();
        let database = client.database("mydb");
        database.collection_with_type("books")
    });
}

#[derive(Debug, Serialize, Deserialize)]
struct Book {
    title: String,
    author: String,
}

impl Book {
    fn new(title: impl ToString, author: impl ToString) -> Self {
        Book {
            title: title.to_string(),
            author: author.to_string(),
        }
    }
}

#[get("/hello/{name}")]
async fn hello(web::Path(name): web::Path<String>) -> impl Responder {
    format!("Hello {}!", name)
}

#[get("/books/{name}")]
async fn books(web::Path(name): web::Path<String>) -> impl Responder {
    let cursor = match BOOKS.get().await.find(doc! { "title":name }, None).await {
        Ok(cursor) => cursor,
        Err(_) => return web::Json(vec![]),
    };
    let books = cursor.try_collect().await.unwrap_or_else(|_| vec![]);
    web::Json(books)
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    if BOOKS.get().await.count_documents(None, None).await.unwrap() <= 0 {
        let docs = vec![
            Book::new("1984", "George Orwell"),
            Book::new("Animal Farm", "George Orwell"),
            Book::new("The Great Gatsby", "F. Scott Fitzgerald"),
        ];
        println!("Inserting books");
        BOOKS.get().await.insert_many(docs, None).await.unwrap();
    }
    let url = "0.0.0.0:8080";
    println!("Serving at: {}", url);
    HttpServer::new(|| App::new().service(hello).service(books))
        .bind(url)?
        .run()
        .await
}
