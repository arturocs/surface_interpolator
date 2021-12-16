use actix_web::{get, web, App, HttpServer, Responder};

#[get("/{name}")]
async fn index(web::Path(name): web::Path<String>) -> impl Responder {
    format!("Hello {}!", name)
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    let url = "0.0.0.0:8080";
    println!("Serving at: {}", url);
    HttpServer::new(|| App::new().service(index))
        .bind(url)?
        .run()
        .await
}
