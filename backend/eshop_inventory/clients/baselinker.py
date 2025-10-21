import json

import requests

from ..api.schemas import InventoryResponse, ProductResponse
from ..settings import EXTRA_FIELD_1_KEY, EXTRA_FIELD_2_KEY, PRICE_GROUP


class BaselinkerClient:
    def __init__(self, api_url: str, api_token: str) -> None:
        self.headers = {"X-BLToken": api_token}
        self.api_url = api_url
        self.session: requests.Session = requests.Session()

    def get_inventories(self) -> list[InventoryResponse]:
        data = {"method": "getInventories"}
        response = self.session.post(self.api_url, data=data, headers=self.headers)
        response = response.json()
        inventories = []
        for inv in response["inventories"]:
            _item = InventoryResponse(
                inventory_id=inv["inventory_id"], name=inv["name"]
            )
            inventories.append(_item)
        return inventories

    def get_product_ids(self, inventory_id: int) -> list[int]:
        params = {"inventory_id": inventory_id}
        data = {"method": "getInventoryProductsList", "parameters": json.dumps(params)}
        response = self.session.post(self.api_url, data=data, headers=self.headers)
        response = response.json()
        return [product["id"] for product in response["products"].values()]

    def get_products_data(
        self, inventory_id: int, product_ids: list[int]
    ) -> list[ProductResponse]:
        params = {"inventory_id": inventory_id, "products": product_ids}
        data = {"method": "getInventoryProductsData", "parameters": json.dumps(params)}
        response = self.session.post(self.api_url, data=data, headers=self.headers)
        response = response.json()

        products = []
        for product_id, product in response["products"].items():
            name = product["text_fields"]["name"]
            extra_1 = product["text_fields"].get(EXTRA_FIELD_1_KEY)
            extra_2 = product["text_fields"].get(EXTRA_FIELD_2_KEY)
            price = product["prices"][PRICE_GROUP]
            _item = ProductResponse(
                id=product_id,
                sku=product["sku"],
                ean=product["ean"],
                name=name,
                extra_field_1=extra_1,
                extra_field_2=extra_2,
                price=price,
            )
            products.append(_item)

        return products

    def update_product(
        self, inventory_id: int, product_id: int, extra_field_2_value: str
    ) -> dict:
        text_fields = {EXTRA_FIELD_2_KEY: extra_field_2_value}
        params = {
            "inventory_id": inventory_id,
            "product_id": product_id,
            "text_fields": text_fields,
        }
        data = {"method": "addInventoryProduct", "parameters": json.dumps(params)}
        response = self.session.post(self.api_url, data=data, headers=self.headers)
        response = response.json()

        if response["status"] == "SUCCESS":
            return {"error": None}
        else:
            return {"error": response["error_message"]}


if __name__ == "__main__":
    from ..settings import API_TOKEN, API_URL

    client = BaselinkerClient(API_URL, API_TOKEN)
    result = client.get_product_ids(833)
    # result = client.get_products_data(833, [2303989, 9556512])
    print(result)
    print(len(result))
