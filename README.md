# symmetrical-journey

> A Vue.js project on Django that allows users to upload their photos, set filters to them and share them

[![Build Status](https://semaphoreci.com/api/v1/stanmd/symmetrical-journey/branches/feature-review/badge.svg)](https://semaphoreci.com/stanmd/symmetrical-journey)
[![Code Health](https://landscape.io/github/NdagiStanley/symmetrical-journey/feature-review/landscape.svg?style=plastic)](https://landscape.io/github/NdagiStanley/symmetrical-journey/ft-setup-repo)
[![Coverage Status](https://coveralls.io/repos/github/NdagiStanley/symmetrical-journey/badge.svg?branch=feature-review)](https://coveralls.io/github/NdagiStanley/symmetrical-journey?branch=feature-review)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for **development** and **testing** purposes.

See **deployment** for notes on how to deploy the project on a live system.

### Prerequisites

You'll need to have the following installed in your local machine to run this application
```Python```, ```Node``` and ```GIT```

### Installing

1. Clone this repository

    RUN ```git clone https://github.com/NdagiStanley/symmetrical-journey.git```

2. CD into the directory

    RUN ```cd symmetrical-journey```

3. Install dependencies of the application/ project

    RUN ```pip install -r requirements.txt``` for django (backend)

    RUN ```npm install``` for vue (frontend)

4. Create a database then update the `settings.py` between lines 128 and 138.

  The built-in database backends are: **'django.db.backends.postgresql' 'django.db.backends.mysql' 'django.db.backends.sqlite3' 'django.db.backends.oracle'** Below is an example using Postgres:

  ```
  else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'mydatabase',
            'USER': 'user',
            'PASSWORD': 'p@ssw0rd',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
  ```
5. Create a file ```.env.yml``` and add the following configuration variables in it.

  ```yml
  SECRET_KEY:
        "Something"
  SOCIAL_AUTH_FACEBOOK_KEY:
        "Something"
  SOCIAL_AUTH_FACEBOOK_SECRET:
        "Something"
  ```
  You can access the `SOCIAL_AUTH_FACEBOOK_SECRET` and the `SOCIAL_AUTH_FACEBOOK_KEY` from the Facebook developer page.

6. To run the server:

    RUN ```python manage.py runserver``` and get to [http://localhost:8000](http://localhost:8000)

7. The project packs a development tool for Vue JS (which supports hot-reloading and webpack bundling).

  For this:

    RUN ```npm run dev``` and get to [http://localhost:8888](http://localhost:8888)

    After editing the Vue components run ```npm run build```

    In the index.html in the templates folder correctly reference the static files and run the django server.

### Testing

To test the backend RUN ```python manage.py test```

To test the frontend (End to End testing) RUN ```npm run e2e```

### Deployment

You'll have to install [**Heroku toolbelt**](https://toolbelt.heroku.com/) for this.

RUN ```heroku local web``` and get to [http://localhost:5000](http://localhost:5000) to see how the application will be on Heroku. Once satisfied, ``heroku push [branch-name]``

### Building blocks

The application hosted [here](https://sjourney.herokuapp.com/) packs a punch.

Pillow is a python package used to manipulate pictures and produce effects like `blurring`, `sharpening` and `pixelate`.

#####Backend
It runs on Django complemented by a REST API made using Django Rest Framework (DRF)

#####Front-end
The front-end is a VueJS based Single Page Application (SPA) using the following tools and libraries:
- `Vue JS` as the View Layer,
- `vue-router` for routing,
- `vuex` for state management,
- `vue-resource` REST-API interfacing plugin,
- `vue-loader` and as mentioned earlier `webpack` which are the *Build tools*

The UI-framework used is `semantic-ui`

----

Copyright AD-2016
###### [Stanley Ndagi](http://techkenyans.org/jamii/stanmd) c/o [Andela](http://andela.com)
