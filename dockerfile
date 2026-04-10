# ---------- Stage 1: Build ----------
FROM python:3.10-slim as builder

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# ---------- Stage 2: Runtime ----------
FROM python:3.10-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /usr/local/lib/python3.10 /usr/local/lib/python3.10
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy app code
COPY . .

# Expose port
EXPOSE 8080

# Run app
CMD ["python", "app.py"]