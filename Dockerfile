# Stage 1: Build Frontend
FROM node:18-alpine AS frontend-build

WORKDIR /app

# Set environment variables
ENV NODE_ENV=production
ENV PATH=/app/node_modules/.bin:$PATH

# Copy package files
COPY frontend/package*.json ./

# Install dependencies
RUN npm install --production --silent && npm cache clean --force

# Copy source code
COPY frontend/ ./

# Build application
RUN npm run build

# Stage 2: Build Backend
FROM python:3.10-slim-bullseye AS backend-build

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Copy requirements
COPY backend/requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy backend source
COPY backend/ ./

# Stage 3: Build Nginx for Frontend
FROM nginx:1.21-alpine AS frontend

# Copy built assets
COPY --from=frontend-build /app/dist /usr/share/nginx/html

# Copy nginx config
COPY docker/nginx.conf /etc/nginx/conf.d/default.conf

# Expose ports
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]

# Stage 4: Build Final Backend
FROM python:3.10-slim-bullseye AS backend

WORKDIR /app

# Copy Python dependencies
COPY --from=backend-build /app/requirements.txt ./
COPY --from=backend-build /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

# Copy backend source
COPY --from=backend-build /app/ ./

# Expose ports
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "info"]
