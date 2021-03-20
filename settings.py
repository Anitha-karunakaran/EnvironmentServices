import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

DATABASE_URL=os.getenv("DATABASE_URL")
TEST_DATABASE_URL=os.getenv("TEST_DATABASE_URL")
API_AUDIENCE = os.getenv("API_AUDIENCE")
AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
CHIEF_OFFICER_JWT = os.getenv("CHIEF_OFFICER_JWT")
SERVICES_MANAGER_JWT = os.getenv("SERVICES_MANAGER_JWT")
