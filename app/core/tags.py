from functools import lru_cache

from pydantic import BaseModel


class RouteTags(BaseModel):
    """
    Base model for app route tags
    """

    # Auth
    AUTH: str = "Auth Endpoints"

    # Carrots
    CARROT: str = "Carrot Endpoints"


@lru_cache
def get_tags():
    """
    Get app rotue tags
    """
    return RouteTags()
