from ..settings import API_TOKEN, API_URL
from .baselinker import BaselinkerClient


def get_baselinker_client():
    return BaselinkerClient(API_URL, API_TOKEN)
