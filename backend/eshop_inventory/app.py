from fastapi import FastAPI

from .api.router import router
from .logs import get_logger
from .settings import IS_LOCAL

# Setup app
is_debug = IS_LOCAL
logger = get_logger("app", is_debug=is_debug)
app = FastAPI(
    title="Eshop Inventory",
    description="System for inventory management",
    version="0.1.0",
    debug=is_debug,
)
logger.debug("FastAPI app created")

# Add API routes
app.include_router(router)

logger.debug("FastAPI routers added")

# For local debugging
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
