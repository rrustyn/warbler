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
