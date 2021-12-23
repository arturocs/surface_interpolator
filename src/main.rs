#[macro_use]
extern crate rocket;
use anyhow::Result;
use async_once::AsyncOnce;
use futures::TryStreamExt;
use lazy_static::lazy_static;
use mongodb::{bson::doc, Client, Collection};
use rocket::serde::json::Json;
use serde::{Deserialize, Serialize};

lazy_static! {
    static ref BOOKS: AsyncOnce<Collection<Book>> = AsyncOnce::new(async {
        let client = Client::with_uri_str("mongodb://mongo:27017").await.unwrap();
        let database = client.database("mydb");
        database.collection::<Book>("books")
    });
}
#[derive(Debug, Serialize, Deserialize, Clone)]
struct ExtraBookInfo {
    pages: u16,
    description: String,
}

impl ExtraBookInfo {
    fn new(pages: u16, description: impl ToString) -> Self {
        Self {
            pages,
            description: description.to_string(),
        }
    }
}

#[derive(Debug, Serialize, Deserialize, Clone)]
struct Book {
    title: String,
    author: String,
    extra_info: Option<ExtraBookInfo>,
}

impl Book {
    fn new(title: impl ToString, author: impl ToString, extra_info: Option<ExtraBookInfo>) -> Self {
        Book {
            title: title.to_string(),
            author: author.to_string(),
            extra_info,
        }
    }
}

#[get("/<name>")]
async fn get_books(name: &str) -> Json<Vec<Book>> {
    let cursor = match BOOKS.get().await.find(doc! { "title":name }, None).await {
        Ok(cursor) => cursor,
        Err(_) => return Json(vec![]),
    };

    Json(cursor.try_collect().await.unwrap_or_else(|_| vec![]))
}

#[rocket::main]
async fn main() -> Result<()> {
    if BOOKS.get().await.count_documents(None, None).await? == 0 {
        let docs = vec![
            Book::new("1984", "George Orwell", None),
            Book::new(
                "Animal Farm",
                "George Orwell",
                Some(ExtraBookInfo::new(112, "The poorly-run Manor Farm near Willingdon, England, is ripened for rebellion...")),
            ),
            Book::new("The Great Gatsby", "F. Scott Fitzgerald", None),
        ];
        println!("Inserting books");
        BOOKS.get().await.insert_many(docs, None).await?;
    }

    rocket::build()
        .mount("/books", routes![get_books])
        .launch()
        .await?;
    Ok(())
}
