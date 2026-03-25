FROM python:3.12-slim

RUN groupadd --gid 1000 appgroup && \
    useradd --uid 1000 --gid appgroup --create-home appuser
WORKDIR /app
COPY --chown=appuser:appgroup app.py .

RUN apt-get update && apt-get install -y curl
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/ || exit 1

EXPOSE 8000
USER appuser
CMD ["python", "app.py"]
