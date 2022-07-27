Minimal Flask App
=================

Basic template to develop an API with Flask, Flask-RESTful and
Flask-RESTful-Swagger

<MIGUEL>
    This is a Flask API template forked from the repositiry of "bonzanini"
    (https://github.com/bonzanini/flask-api-template)

Usage
-----

Clone the repo:

    git clone https://github.com/INGENmigs/flask-api-template
              (git@github.com:INGENmigs/flask-api-template.git)
    cd flask-api-template

Create virtualenv:

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python setup.py develop # or install if you prefer

Run the sample server

    python runserver.py

Try the endpoints:

    curl -XGET http://localhost:5000/
    curl -XPOST -H "Content-Type: application/json" http://localhost:5000/hello -d '{"name": "World"}'

Swagger docs available at `http://localhost:5000/api/spec.html`


License
-------

MIT, see LICENSE file

