# Use the official FastAPI image based on Python
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Set working directory
WORKDIR /app

# Copy the FastAPI application code
COPY main.py .

# Install MySQL connector
RUN pip install mysql-connector-python fastapi pydantic

# Expose port 80 for FastAPI
EXPOSE 80

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
