FROM rust:alpine as build-env
WORKDIR /app
COPY . /app
RUN apk add --no-cache musl-dev && \
    cargo build --release && \
    strip -s /app/target/release/surface_interpolator

FROM gcr.io/distroless/static:latest
COPY --from=build-env /app/target/release/surface_interpolator /
ENV ROCKET_ADDRESS=0.0.0.0
CMD ["./surface_interpolator"]