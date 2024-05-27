SHELL := /usr/bin/env bash

IMAGE := shipstation_client
VERSION := latest

#! An ugly hack to create individual flags
ifeq ($(STRICT), 1)
	POETRY_COMMAND_FLAG =
	PIP_COMMAND_FLAG =
	SAFETY_COMMAND_FLAG =
	BANDIT_COMMAND_FLAG =
	SECRETS_COMMAND_FLAG =
	BLACK_COMMAND_FLAG =
	DARGLINT_COMMAND_FLAG =
	ISORT_COMMAND_FLAG =
	MYPY_COMMAND_FLAG =
else
	POETRY_COMMAND_FLAG = -
	PIP_COMMAND_FLAG = -
	SAFETY_COMMAND_FLAG = -
	BANDIT_COMMAND_FLAG = -
	SECRETS_COMMAND_FLAG = -
	BLACK_COMMAND_FLAG = -
	DARGLINT_COMMAND_FLAG = -
	ISORT_COMMAND_FLAG = -
	MYPY_COMMAND_FLAG = -
endif

##! Please tell me how to use `for loops` to create variables in Makefile :(
##! If you have better idea, please PR me in https://github.com/TezRomacH/python-package-template

ifeq ($(POETRY_STRICT), 1)
	POETRY_COMMAND_FLAG =
else ifeq ($(POETRY_STRICT), 0)
	POETRY_COMMAND_FLAG = -
endif

ifeq ($(PIP_STRICT), 1)
	PIP_COMMAND_FLAG =
else ifeq ($(PIP_STRICT), 0)
	PIP_COMMAND_FLAG = -
endif

ifeq ($(SAFETY_STRICT), 1)
	SAFETY_COMMAND_FLAG =
else ifeq ($SAFETY_STRICT), 0)
	SAFETY_COMMAND_FLAG = -
endif

ifeq ($(BANDIT_STRICT), 1)
	BANDIT_COMMAND_FLAG =
else ifeq ($(BANDIT_STRICT), 0)
	BANDIT_COMMAND_FLAG = -
endif

ifeq ($(SECRETS_STRICT), 1)
	SECRETS_COMMAND_FLAG =
else ifeq ($(SECRETS_STRICT), 0)
	SECRETS_COMMAND_FLAG = -
endif

ifeq ($(BLACK_STRICT), 1)
	BLACK_COMMAND_FLAG =
else ifeq ($(BLACK_STRICT), 0)
	BLACK_COMMAND_FLAG = -
endif

ifeq ($(DARGLINT_STRICT), 1)
	DARGLINT_COMMAND_FLAG =
else ifeq (DARGLINT_STRICT), 0)
	DARGLINT_COMMAND_FLAG = -
endif

ifeq ($(ISORT_STRICT), 1)
	ISORT_COMMAND_FLAG =
else ifeq ($(ISORT_STRICT), 0)
	ISORT_COMMAND_FLAG = -
endif


ifeq ($(MYPY_STRICT), 1)
	MYPY_COMMAND_FLAG =
else ifeq ($(MYPY_STRICT), 0)
	MYPY_COMMAND_FLAG = -
endif

#! The end of the ugly part. I'm really sorry

.PHONY: download-poetry
download-poetry:
	curl -sSL https://install.python-poetry.org | python3 -

.PHONY: install
install:
	poetry lock -n
	poetry install -n
ifneq ($(NO_PRE_COMMIT), 1)
	poetry run pre-commit install
endif

.PHONY: check-safety
check-safety:
	$(POETRY_COMMAND_FLAG)@echo -e "Checking poetry..."
	$(POETRY_COMMAND_FLAG)poetry check --quiet

	$(PIP_COMMAND_FLAG)@echo -e "\nChecking pip..."
	$(PIP_COMMAND_FLAG)pip check

	$(BANDIT_COMMAND_FLAG)@echo -e "\nChecking bandit..."
	$(BANDIT_COMMAND_FLAG)poetry run bandit --silent --severity-level medium --recursive shipstation_client/

	$(SAFETY_COMMAND_FLAG)@echo -e "\nChecking safety..."
	$(SAFETY_COMMAND_FLAG)poetry run safety --disable-optional-telemetry scan --detailed-output

.PHONY: check-style
check-style:
	$(BLACK_COMMAND_FLAG)@echo -e "Checking black..."
	$(BLACK_COMMAND_FLAG)poetry run black --config pyproject.toml --diff --check ./

	$(DARGLINT_COMMAND_FLAG)@echo -e "\nChecking darglint..."
	$(DARGLINT_COMMAND_FLAG)poetry run darglint --verbosity 2 **/*.py

	$(ISORT_COMMAND_FLAG)@echo -e "\nChecking isort..."
	$(ISORT_COMMAND_FLAG)poetry run isort . --settings-path pyproject.toml --check-only

	$(MYPY_COMMAND_FLAG)@echo -e "\nChecking mypy..."
	$(MYPY_COMMAND_FLAG)poetry run mypy tests/

.PHONY: codestyle
codestyle:
	poetry run pre-commit run --all-files

.PHONY: check-style
mypy:
	poetry run mypy shipstation/

.PHONY: test
test:
	@echo -e "Running tests..."
	poetry run pytest

.PHONY: lint
lint: test check-style check-safety

# Example: make docker VERSION=latest
# Example: make docker IMAGE=some_name VERSION=0.1.0
.PHONY: docker
docker:
	@echo Building docker $(IMAGE):$(VERSION) ...
	docker build \
		--tag $(IMAGE):$(VERSION) . \
		--file ./docker/Dockerfile \
		--no-cache

# Example: make clean_docker VERSION=latest
# Example: make clean_docker IMAGE=some_name VERSION=0.1.0
.PHONY: clean_docker
clean_docker:
	@echo Removing docker $(IMAGE):$(VERSION) ...
	docker rmi --force $(IMAGE):$(VERSION)

.PHONY: clean
clean: clean_docker
