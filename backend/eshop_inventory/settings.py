import os

# Runtime
ENVIRONMENT = os.getenv("ENVIRONMENT", "local")
IS_LOCAL = ENVIRONMENT == "local"

# API
API_URL = "https://api.baselinker.com/connector.php"
API_TOKEN = os.environ["API_TOKEN"]

# Data
EXTRA_FIELD_1_KEY = "extra_field_467"
EXTRA_FIELD_2_KEY = "extra_field_484"
PRICE_GROUP = "849"
