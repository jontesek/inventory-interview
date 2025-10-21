from pydantic import BaseModel


class InventoryResponse(BaseModel):
    inventory_id: int
    name: str


# class OrderCreate(BaseModel):
#     client_id: int
#     contact_phone: str
#     note_for_driver: str | None
#     order_items: list[OrderItemCreate]


# class OrderCreateResponse(BaseModel):
#     id: int
#     email: str
