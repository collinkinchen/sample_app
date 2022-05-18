# sample_app

## Tech Stack

Python3 with Flask <br />
Database: MySQL <br />

## Requirements

Python3 <br />
MySQL DB <br />

## Install

```
cd sample_app
```
Edit Makefile and ensure FLASK_APP name and FLASK_ENV is correct <br />
Edit config.py and ensure you mysql db connection is correct <br />
<br />
Build virtual environment and install packages:
```
make
```
Setup database tables using python3 CLI
```
source venv/bin/activate
python3
>>> from myproject import db, create_app, models
>>> db.create_all(app=create_app()) 
```

Start the application
```
make run
```

## Test
functional testing of endpoints, response codes and API payloads can be done via unittest or pytest modules <br />
```
cd sample_app
python3 test.py -v
```


## Monitoring
Monitoring can be setup using OpenTelemetry
https://signoz.io/blog/opentelemetry-flask/

## Improvments

- Better UI with cleaner stylying and navbar
- Pictures to go along with favorite food
