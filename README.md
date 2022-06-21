# STARS-APP

Web application for STARS Explorer that allows sustainability practitioner to explorer data from STARS, which is The Sustainability Tracking, Assessment & Rating System. (https://stars.aashe.org/)

Please also note the Web API that it uses: https://github.com/Romantic-of-TextMining/STARS_API

## Install

Install this application by cloning the *relevant branch* and use bundler to install specified gems from `Gemfile.lock`:

```shell
$ python3 -m pip install -r requirements.txt
```

## Execute

Launch the application using:

```shell
export FLASK_APP=stars.py
flask run
```

The application expects the API application to also be running
