FROM python:3.12-alpine

RUN addgroup -g 1000 appgroup && adduser -D -u 1000 -G appgroup appuser
RUN mkdir /app && chown appuser:appgroup /app
WORKDIR /app
COPY --chown=appuser:appgroup app.py .


EXPOSE 8000
USER appuser
CMD ["python","-u", "app.py"]
