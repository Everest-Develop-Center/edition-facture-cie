# Invoice Generation Service

A FastAPI application for generating and downloading PDF invoices.

## Features

- REST API for invoice generation
- PDF invoice generation from HTML templates
- Token-based authentication

## Requirements

- Python 3.11+
- Docker (for containerized deployment)

## Local Development

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Install Playwright and browsers:
   ```
   pip install playwright
   playwright install chromium
   playwright install-deps chromium
   ```
4. Run the application:
   ```
   uvicorn main:app --reload
   ```

## Docker Deployment

### Build the Docker image

```bash
docker build -t invoice-service .
```

### Run the Docker container

```bash
docker run -p 8000:8000 invoice-service
```

### Using Docker Compose (Recommended for Development)

```bash
docker-compose up
```

This will:
- Build the Docker image if it doesn't exist
- Mount the temp and templates directories as volumes
- Enable hot-reload for code changes
- Set up a healthcheck for the service

The application will be available at http://localhost:8000

### API Endpoints

- `GET /`: Root endpoint (Hello World)
- `GET /download-invoice/{invoice_id}`: Download a PDF invoice (requires authentication token)

## Authentication

The API uses token-based authentication. Include your token in the Authorization header:

```
Authorization: Bearer YOUR_TOKEN
```
