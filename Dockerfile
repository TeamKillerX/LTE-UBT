FROM python:3.10-slim

RUN apt-get update -qq && \
    apt-get install -y --no-install-recommends \
        ffmpeg curl git gnupg2 unzip wget && \
    pip install --no-cache-dir uv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

RUN uv pip install --system --requirements requirements.lock

CMD ["uv", "run", "python", "-m", "LTE-UBT"]
