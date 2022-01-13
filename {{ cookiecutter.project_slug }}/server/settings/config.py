import os
from databases import DatabaseURL

PROJECT_NAME = "{{cookiecutter.project_slug}}"
MONGODB_URL = os.getenv("MONGODB_URL", "")
if not MONGODB_URL:
    MONGODB_URL = DatabaseURL(
        "mongodb://localhost:27017/"
    )
else:
    MONGODB_URL = DatabaseURL(MONGODB_URL)
