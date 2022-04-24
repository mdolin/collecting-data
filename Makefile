# I suggest all future developer to treat next few
# lines as an opportunity to learn a thing or two about GNU make ;)
python_version := $(shell \
  python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))' \
)

unit_test_targets := $(shell find tests/unit -name '*.py')
integration_test_targets := $(shell ls tests/integration/)


.PHONY: help
help:
	@echo Available targets:
	@fgrep "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sort

# Developer convenience targets

.PHONY: format
format:  ## Format python code with black
	black main.py database tests/unit

.PHONY: clean
clean:  ## Remove all auto-generated files
	rm -rf tests/output

.PHONY: $(unit_test_targets)
$(unit_test_targets):
	ansible-test units --requirements --python $(python_version) $@

.PHONY: $(integration_test_targets)
$(integration_test_targets):
	ansible-test integration --requirements --python $(python_version) --diff $@

# Things also used in CI/CD

.PHONY: sanity
sanity:  ## Run sanity tests
	pip install -r sanity.requirements
	black --check --diff --color main.py database tests/unit
	flake8

.PHONY: units
units:  ## Run unit tests
	

.PHONY: integration
integration:  ## Run integration tests

