freeze:
	pip freeze > requirements.txt

run:
	flask run

webpack-build:
	npx webpack build --config webpack.config.js --mode production

webpack-watch-prod:
	npx webpack watch --config webpack.config.js --mode production

webpack-watch-dev:
	npx webpack watch --config webpack.config.js

mypy:
	cd ./web && mypy ./ --ignore-missing-imports

pylint:
	pylint ./web
