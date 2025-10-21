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


# class OrderCreate(BaseModel):
#     client_id: int
#     contact_phone: str
#     note_for_driver: str | None
#     order_items: list[OrderItemCreate]


# class OrderCreate(BaseModel):
#     client_id: int
#     contact_phone: str
#     note_for_driver: str | None
#     order_items: list[OrderItemCreate]


# class OrderCreateResponse(BaseModel):
#     id: int
#     email: str
