--shell=/usr/bin/env bash
.PHONY: all clean build develop install test format

build:
	pdm build

test:install
	./bin/test

develop:
	pdm install

install:build
	pdm install --production

publish:
	git add .
	git commit
	git push

clean:
	rm -v -rf .tox .eggs/ eggs/ dbs/ tmp/ .pytest_cache/ .mypy_cache/ .scrapy/ logs/ *.egg-info/ dist/ build/ *.log nohup.out nohup.err _trial_temp/ .eggs/ .glab-cli/
	find . -name "*.pyc" -type f -exec rm -v -rf {} \+
	find . -name "__pycache__" -type d -exec rm -v -rf {} \+

format:
	isort -vvv src tests
	black -vvv src tests
	dprint --verbose -c config/dprint/dprint.json fmt

all: clean test install
