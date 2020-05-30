#!/bin/sh
~/.env/bin/pip install -r app/requirements-test.txt
cd ~/app
~/.env/bin/pytest --cov-report term-missing:skip-covered --cov=homework
