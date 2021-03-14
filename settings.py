import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

FLASK_APP=os.getenv("FLASK_APP")
FLASK_ENV=os.getenv("FLASK_ENV")
DATABASE_URL=os.getenv("DATABASE_URL")
TEST_DATABASE_URL=os.getenv("TEST_DATABASE_URL")
