test:
	coverage run -m  unittest
	coverage report -m
.PHONY: test
