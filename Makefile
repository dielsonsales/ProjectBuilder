run:
	python src/projectbuilder.py

lint:
	flake8 src

format:
	black src --line-length 79
