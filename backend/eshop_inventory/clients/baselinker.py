import requests

from ..api.schemas import InventoryResponse


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


if __name__ == "__main__":
    from ..settings import API_TOKEN, API_URL

    client = BaselinkerClient(API_URL, API_TOKEN)
    result = client.get_inventories()
    print(result)
