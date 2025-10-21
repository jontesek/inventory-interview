from fastapi import APIRouter, Depends

from ..clients.baselinker import BaselinkerClient
from ..clients.dependencies import get_baselinker_client
from .schemas import InventoryResponse

router = APIRouter(prefix="/api")


@router.get("/inventories", response_model=list[InventoryResponse])
def get_inventories(
    base_client: BaselinkerClient = Depends(get_baselinker_client),
):
    return base_client.get_inventories()


@router.get("/inventory-products/{inventory_id}", response_model=[])
def get_client(
    inventory_id: int,
    base_client: BaselinkerClient = Depends(get_baselinker_client),
):
    product_ids = base_client.get_product_ids(inventory_id)
    return base_client.get_products_data(inventory_id, product_ids)


# @router.post("/orders", response_model=OrderCreateResponse)
# def create_order(
#     data: OrderCreate,
#     db: Session = Depends(get_db),
#     mailer: Mailer = Depends(get_mailer),
# ):
#     repo = OrderRepository(db)

#     # Save to DB
#     try:
#         resp = repo.create_order(data)
#     except EntityNotFoundError as e:
#         raise HTTPException(status_code=404, detail=str(e)) from e
#     except OrderPiecesError as e:
#         raise HTTPException(status_code=422, detail=str(e)) from e

#     # Send email confirmation
#     conf = create_order_confirmation(resp)
#     try:
#         mailer.send_email(
#             to=resp["client_email"],
#             subject=conf["subject"],
#             message_text=conf["message"],
#         )
#     except Exception as e:
#         msg = "Could not send order confirmation email, transaction aborted."
#         raise HTTPException(status_code=500, detail=msg) from e

#     db.commit()

#     return OrderCreateResponse(id=resp["order_id"], email=resp["client_email"])
