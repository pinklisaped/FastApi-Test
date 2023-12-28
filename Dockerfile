FROM python:3.11.2-alpine3.17

# Set work directory
WORKDIR /app
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN \
    python -m venv /venv && \
    /venv/bin/pip install -r requirements.txt --no-cache-dir

# Copy app
COPY . /app

EXPOSE 8000

# Run app
ENTRYPOINT ["/venv/bin/uvicorn", "main:app", "--host", "0.0.0.0"]