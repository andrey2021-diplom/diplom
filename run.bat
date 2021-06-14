@echo off
echo Running Debug Server

set FLASK_APP=app
set FLASK_DEBUG=1

start http://localhost/

flask run --port 80
