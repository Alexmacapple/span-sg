# Dockerfile
FROM squidfunk/mkdocs-material:latest
WORKDIR /docs
RUN pip install mkdocs-pdf-export-plugin mkdocs-with-pdf
EXPOSE 8000
CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8000"]
