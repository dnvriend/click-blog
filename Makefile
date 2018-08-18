.PHONY: init remove run

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

init: ## creates a new python environment containing all dependencies
	pipenv install --dev

remove: ## remove the python environment
	pipenv --rm

clean: ## removes all build artifacts
	rm -rf buckets.egg-info build dist

run: ## runs buckets
	pipenv run python buckets/buckets.py

run-help: ## runs buckets and asks for help
	pipenv run python buckets/buckets.py --help

run-ls: ## print all buckets
	pipenv run python buckets/buckets.py ls

run-du: ## print bucket usage
	pipenv run python buckets/buckets.py du

run-count: ## count the number of buckets
	pipenv run python buckets/buckets.py count

dist: ## create a distribution
	pipenv run python setup.py bdist_wheel

install: ## install buckets
	pip install dist/buckets-0.1-py3-none-any.whl

uninstall: ## uninstall buckets
	pip uninstall --yes dist/buckets-0.1-py3-none-any.whl