DATABASE = {
    "USER": "postgres",
    "PASSWORD": "password",
    "HOST": "localhost",
    "PORT": "5432",
    "NAME": "autoresume",
}

# Gemini Configuration
GEMINI_API_KEY = "AIzaSyC4mgjXyVy7ufdkxew6SRYCDxuiR58iD7Y"

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DATABASE['USER']}:{DATABASE['PASSWORD']}@"
    f"{DATABASE['HOST']}:{DATABASE['PORT']}/{DATABASE['NAME']}"
)