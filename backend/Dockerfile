FROM python:3.12-slim

RUN groupadd --gid 1000 appgroup && \
    useradd --uid 1000 --gid appgroup --create-home appuser
WORKDIR /app
COPY --chown=appuser:appgroup app.py .


EXPOSE 8000
USER appuser
CMD ["python", "app.py"]
