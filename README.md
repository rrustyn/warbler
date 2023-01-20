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



Running and Organizing Tests
============================

View (Route) and Model tests will live in separate files within a test directory
in each app ::

  messages/tests/test_views.py
  messages/tests/test_models.py

Use the -v flag for verbose test output

Run tests within a test directory ::

  python -m unittest
  python -m unittest -v

Run a single test file within a test directory ::

  python -m unittest TEST_FILE_NAME.py
  python -m unittest -v TEST_FILE_NAME.py
