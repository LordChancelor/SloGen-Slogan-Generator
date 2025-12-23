
FROM python:3.10-slim


WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create a writable cache directory for Hugging Face (Required for permission errors)
RUN mkdir -p /app/cache
os.environ['HF_HOME'] = '/app/cache'
RUN chmod -R 777 /app

# Run the application
CMD ["python", "app.py"]