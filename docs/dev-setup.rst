Development Environment Setup
=============================

Add a `.env` file in the top level directory and include the following ::

  DATABASE_URL=postgresql:///warbler
  DATABASE_URL_TEST=postgresql:///warbler-test
  FLASK_APP=warbler
  SECRET_KEY=so_secret

You'll need Python3 and PostgreSQL ::

  python3 -m venv venv
  source venv/bin/activate
  pip3 install -r requirements.txt

  createdb warbler
  createdb warbler-test

Install warbler as a python package in the top level directory ::

  pip install -e .

After installing warbler delete the warbler.egg-info/ directory ::

  rm -rf warbler.egg-info/

When you need to add dependencies to requirements.txt, don't include the
warbler package as a dependency. To ensure it's not added, update
requirements.txt like this ::

  pip freeze | grep -v github.com > requirements.txt
