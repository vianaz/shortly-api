API_IMAGE=shortly_api
DB_IMAGE=shortly_db
PGADMIN_IMAGE=shortly_pgadmin
COMPOSE_FILE=docker/docker-compose-dev.yml
TAG?=latest
PWD=$(shell pwd)
WORKDIR=app
ENV_FILE=.env
USER=$(shell id -u):$(shell id -g)

.PHONY:	all build-dev-images

all:	build-image

build-images: ## Build Docker Images
	$(info Docker - Building Image ...)
	@docker compose -f $(COMPOSE_FILE) --env-file $(ENV_FILE) create $(API_IMAGE) $(DB_IMAGE) $(PGADMIN_IMAGE)

init-database: ## Run Database
	$(info Docker - Running Database ...)
	@docker compose -f $(COMPOSE_FILE) --env-file $(ENV_FILE) start $(DB_IMAGE)

stop-database: ## Stop Database
	$(info Docker - Stopping Database ...)
	@docker compose -f $(COMPOSE_FILE) --env-file $(ENV_FILE) stop $(DB_IMAGE)

logs-database: ## Show Database Logs
	$(info Docker - Showing Database Logs ...)
	@docker compose -f $(COMPOSE_FILE) --env-file $(ENV_FILE) logs -f $(DB_IMAGE)

init-pgadmin: ## Run PgAdmin
	$(info Docker - Running PgAdmin ...)
	@docker compose -f $(COMPOSE_FILE) --env-file $(ENV_FILE) start $(PGADMIN_IMAGE)

stop-pgadmin: ## Stop PgAdmin
	$(info Docker - Stopping PgAdmin ...)
	@docker compose -f $(COMPOSE_FILE) --env-file $(ENV_FILE) stop $(PGADMIN_IMAGE)

logs-pgadmin: ## Show PgAdmin Logs
	$(info Docker - Showing PgAdmin Logs ...)
	@docker compose -f $(COMPOSE_FILE) --env-file $(ENV_FILE) logs -f $(PGADMIN_IMAGE)

install-deps: ## Install Dependencies
	$(info Docker - Installing Dependencies ...)
	@docker compose -f $(COMPOSE_FILE) --env-file $(ENV_FILE) run --rm $(API_IMAGE) poetry install && sudo chown -R $(USER) .venv

init-api: ## Run API
	$(info Docker - Running API ...)
	@docker compose -f $(COMPOSE_FILE) --env-file $(ENV_FILE) start $(API_IMAGE)

stop-api: ## Stop API
	$(info Docker - Stopping API ...)
	@docker compose -f $(COMPOSE_FILE) --env-file $(ENV_FILE) stop $(API_IMAGE)

logs-api: ## Show API Logs
	$(info Docker - Showing API Logs ...)
	@docker compose -f $(COMPOSE_FILE) --env-file $(ENV_FILE) logs -f $(API_IMAGE)

clear-images: ## Clear Docker Images
	$(info Docker - Clearing Images ...)
	@docker compose -f $(COMPOSE_FILE) --env-file $(ENV_FILE) down --rmi all

top: ## Show Docker Containers
	$(info Docker - Showing Containers ...)
	@docker compose -f $(COMPOSE_FILE) --env-file $(ENV_FILE) top

help: ## Show this help.
# `help' function obtained from GitHub gist: https://gist.github.com/prwhite/8168133?permalink_comment_id=4160123#gistcomment-4160123
	@echo Shortly API
	@awk 'BEGIN {FS = ": .*##"; printf "\nUsage:\n  make \033[36m\033[0m\n"} /^[$$()% 0-9a-zA-Z_-]+(\\:[$$()% 0-9a-zA-Z_-]+)*:.*?##/ { gsub(/\\:/,":", $$1); printf "  \033[36m%-16s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

.DEFAULT_GOAL=help
