# Django React/Redux Base Project

This repository includes a boilerplate project. It uses Django as backend and React as frontend.

Technologies:

**Frontend**

* [React](https://github.com/facebook/react)
* [React Router](https://github.com/ReactTraining/react-router)
* [Babel](http://babeljs.io)
* [Webpack](http://webpack.github.io)
* [Webpack Dev Middleware](http://webpack.github.io/docs/webpack-dev-middleware.html)
* [Clean Webpack Plugin](https://github.com/johnagan/clean-webpack-plugin)
* [Redux](https://github.com/reactjs/redux)
* [Redux Dev Tools](https://github.com/gaearon/redux-devtools)
* [Redux Thunk](https://github.com/gaearon/redux-thunk)
* [React Router Redux](https://github.com/reactjs/react-router-redux)
* [fetch](https://github.com/github/fetch)
* [tcomb form](https://github.com/gcanti/tcomb-form)
* [style-loader](https://github.com/webpack/style-loader), [sass-loader](https://github.com/jtangelder/sass-loader) and [less-loader](https://github.com/webpack-contrib/less-loader)
* [font-awesome-webpack](https://github.com/gowravshekar/font-awesome-webpack)
* [bootstrap-loader](https://github.com/shakacode/bootstrap-loader)
* [ESLint](http://eslint.org), [Airbnb Javascript/React Styleguide](https://github.com/airbnb/javascript), [Airbnb CSS / Sass Styleguide](https://github.com/airbnb/css) 
* [eslint-plugin-import](https://github.com/benmosher/eslint-plugin-import)
* [mocha](https://mochajs.org/)
* [Enzyme](http://airbnb.io/enzyme/)
* [redux-mock-store](https://github.com/arnaudbenard/redux-mock-store)
* [expect](https://github.com/mjackson/expect)
* [Nock](https://github.com/pgte/nock)
* [istanbul](https://github.com/gotwarlost/istanbul)

**Backend**

* [Django](https://www.djangoproject.com/)
* [Django REST framework](http://www.django-rest-framework.org/)
* [Django REST Knox](https://github.com/James1345/django-rest-knox)
* [WhiteNoise](http://whitenoise.evans.io/en/latest/django.html)
* [Prospector](http://prospector.landscape.io/en/master/)
* [pytest](http://pytest.org/latest/)
* [Responses](https://github.com/getsentry/responses)


## Retrieve code

* `$ git clone `

## Installation

You have two ways of running this project: Using the Dockers scripts or running directly in the console.

### Running NO DOCKER

* You must create a environment variable on your machine, example in `.env.temp`.

**NodeJS tooling**

* `$ wget -qO- https://deb.nodesource.com/setup_6.x | sudo bash -`
* `$ apt-get install --yes nodejs`
* `$ curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -`
* `$ echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list`
* `$ sudo apt-get update && sudo apt-get install yarn`

**Compile and run project**

There are commands you need to compile javascript and run project. Ideally `yarn run dev` should be run in another console because it blocks it.

* `$ yarn `
* `$ yarn run dev`

* `$ virtualenv -p /usr/bin/python3 virtualenv`
* `$ source virtualenv/bin/activate`
* `$ pip install -r py-requirements/dev.txt`

* `$ cd src`
* `$ python manage.py migrate`
* `$ python manage.py loaddata fixtures/admin_fixtures.json` #optional
* `$ python manage.py runserver`

Then open your browser the page: http://localhost:8000/ If all goes ok you should see a React single page app. 


### Running DOCKER

* You must create a file with environment variable example in `.env.temp`.
* `$ cp .env.temp .env`

* Install [Docker](https://www.docker.com/products/overview) and [Docker Compose](https://docs.docker.com/compose/install/).
* `$ docker-compose build`
* `$ docker-compose up`

To stop the development server:

* `$ docker-compose stop`

Stop Docker development server and remove containers, networks, volumes, and images created by up.

* `$ docker-compose down`

You can access shell in a container

* `$ docker ps  # get the name from the list of running containers`
* `$ docker exec -it yourCatalogName_frontend_1 bash`

The database can be accessed @localhost:5433

* `$ psql -h localhost -p 5433 -U postgres db_name`


## Accessing Website

On local host url http://localhost:8000


## Testing

To make sure the code respects all coding guidelines you should run test scripts before pushing any code.

Frontend (javascript tests)

local
* `$ npm run mocha`

docker
* `$ make docker-test-frontend`

Backend (django/python tests)

local
* `$ pytest --cov=.`

docker
* `$ make docker-test-backend`


## Makefile command

For local setup :
* `lint` - python linter
* `install-dev-requirements` - install python dev requirements
* `run-migrations` - apply migration to running django
* `tests-python` - run tests for python

For docker setup :
* `docker-lint-flake8` - flake8 python linter on docker
* `docker-lint-pydocstyle` - pydocstyle python linter on docker
* `docker-install-dev-requirements` - install python dev requirements on docker
* `docker-start-db` - build and start database docker
* `docker-start-bg` - build and start backend docker
* `docker-start-redis` - build and start redis docker
* `docker-start-frontend` - build and start frontend docker
* `docker-dev-start-all` - start all dockers
* `docker-test` - run tests for python and js in docker
* `docker-test-backend` - run tests for python in docker
* `docker-test-frontend` - run tests for js in docker
* `docker-makemigrations` - create new migrations for django in docker
* `docker-migrations` - apply migration to running django in docker
* `docker-reset-db` - recreating database docker
* `docker-add-admin` - create admin user
