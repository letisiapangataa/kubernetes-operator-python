FROM python:3.11-slim
WORKDIR /app
COPY operator/ ./operator/
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --no-root
CMD ["poetry", "run", "python", "-m", "operator.main"]
