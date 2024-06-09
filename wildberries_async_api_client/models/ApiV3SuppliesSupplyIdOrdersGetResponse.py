from typing import *

from pydantic import BaseModel, Field

from .SupplyOrder import SupplyOrder


class ApiV3SuppliesSupplyIdOrdersGetResponse(BaseModel):
    """
    None model

    """

    orders: Optional[List[Optional[SupplyOrder]]] = Field(alias="orders", default=None)
