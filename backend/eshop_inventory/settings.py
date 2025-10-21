import os

# Runtime
ENVIRONMENT = os.getenv("ENVIRONMENT", "local")
IS_LOCAL = ENVIRONMENT == "local"

# API
API_URL = "https://api.baselinker.com/connector.php"
API_TOKEN = os.environ["API_TOKEN"]
