SET FLASK_APP=app
SET FLASK_ENV=development
SET FLASK_DEBUG=True
REM OVERRIDE THE DATABASE_URL AND TEST_DATABASE_URL if required
REM SET DATABASE_URL=postgresql://postgres:postgres@localhost:5432/envsrvdb
REM SET TEST_DATABASE_URL=postgresql://postgres:postgres@localhost:5432/test_envsrvdb
flask run