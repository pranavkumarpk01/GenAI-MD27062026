FROM python:3.12-slim

WORKDIR /app

# System deps needed to build some Python wheels (e.g. pypdf, qdrant-client transitive deps)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps first for better layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Defaults; override at `docker run` time to point at your Qdrant/Ollama hosts
ENV QDRANT_HOST=qdrant \
    QDRANT_PORT=6333 \
    OLLAMA_BASE_URL=http://host.docker.internal:11434 \
    PDF_PATH=hr_policy_detailed_5_pages.pdf

# No web server here — this image just runs the CLI scripts.
# Default to ingestion; override the command to run query.py instead.
CMD ["python", "ingestion.py"]
