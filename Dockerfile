FROM rust:alpine as build-env
WORKDIR /app
COPY . /app
RUN apk add --no-cache musl-dev && \
    cargo build --release && \
    strip -s /app/target/release/surface_interpolator

FROM gcr.io/distroless/static:latest
EXPOSE 8080
COPY --from=build-env /app/target/release/surface_interpolator /
CMD ["./surface_interpolator"]