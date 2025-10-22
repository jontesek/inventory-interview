from fastapi import FastAPI, Request

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


# For Https redirect error on Prod
@app.middleware("http")
async def patch_scheme_from_proxy(request: Request, call_next):
    forwarded_proto = request.headers.get("x-forwarded-proto")
    if forwarded_proto:
        request.scope["scheme"] = forwarded_proto
    return await call_next(request)


# Add API routes
app.include_router(router)

logger.debug("FastAPI routers added")

# For local debugging
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)  # noqa: S104
