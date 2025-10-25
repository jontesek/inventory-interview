from fastapi import APIRouter, Depends, HTTPException

from ..clients.baselinker import BaselinkerClient
from ..clients.dependencies import get_baselinker_client
from .schemas import InventoryResponse, ProductResponse, ProductUpdate

router = APIRouter(prefix="/api")


@router.get("/inventories", response_model=list[InventoryResponse])
def get_inventories(
    base_client: BaselinkerClient = Depends(get_baselinker_client),
):
    return base_client.get_inventories()


@router.get("/inventory-products/{inventory_id}", response_model=[ProductResponse])
def get_client(
    inventory_id: int,
    base_client: BaselinkerClient = Depends(get_baselinker_client),
):
    product_ids = base_client.get_product_ids(inventory_id)
    return base_client.get_products_data(inventory_id, product_ids)


@router.put("/products", response_model=dict)
def create_order(
    data: ProductUpdate,
    base_client: BaselinkerClient = Depends(get_baselinker_client),
):
    response = base_client.update_product(
        data.inventory_id, data.product_id, data.extra_field_2
    )
    error_msg = response.get("error")

    if error_msg:
        raise HTTPException(status_code=400, detail=error_msg)

    return {"status": "success"}


@router.get("/health", response_model=dict)
def health_check():
    return {"status": "ok"}
