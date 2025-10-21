from pydantic import BaseModel


class InventoryResponse(BaseModel):
    inventory_id: int
    name: str


class ProductResponse(BaseModel):
    id: int
    sku: str
    ean: str
    name: str
    price: float
    extra_field_1: str | None
    extra_field_2: str | None


class ProductUpdate(BaseModel):
    inventory_id: int
    product_id: int
    extra_field_2: str
