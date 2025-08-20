IMAGE ?= ghcr.io/you/backup-operator:latest

.PHONY: build push kind-load test lint

build:
	docker build -t $(IMAGE) .

push:
	docker push $(IMAGE)

kind-load:
	kind load docker-image $(IMAGE)

lint:
	poetry run flake8 operator/

test:
	poetry run pytest tests/unit
