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
```
make run
```

## Test
functional testing of endpoints, response codes and API payloads can be done via unittest or pytest modules
Example: get "/" - assert 200

## Monitoring
Monitoring can be setup using OpenTelemetry
https://signoz.io/blog/opentelemetry-flask/

## Improvments

- Better UI with cleaner stylying and navbar
- Pictures to go along with favorite food