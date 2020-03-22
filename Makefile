format:
	black .
	isort -y

dev:
	pip install -r requirements.txt
	pre-commit install
