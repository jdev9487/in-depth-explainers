# FROM jdev9487/latex:latest as build
FROM kjarosh/latex:2025.1-medium as build

WORKDIR /app

COPY . .

RUN sh ./scripts/build-pdfs.sh

FROM nginx

COPY --from=build /app/output /www/media
COPY ./nginx.conf /etc/nginx/nginx.conf

CMD ["/usr/sbin/nginx", "-g", "daemon off;"]