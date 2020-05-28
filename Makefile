
.PHONY: build
build:
	docker build -f .devcontainer/Dockerfile . -t ignas-homework:latest

.PHONY: run
run:
	docker run --rm -ti -p 6544:6544 ignas-homework:latest