# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class NmReportGroupedHistoryResponseDataInnerHistoryInner(BaseModel):
    """
    NmReportGroupedHistoryResponseDataInnerHistoryInner
    """ # noqa: E501
    dt: Optional[date] = None
    open_card_count: Optional[StrictInt] = Field(default=None, description="Количество переходов в карточку товара", alias="openCardCount")
    add_to_cart_count: Optional[StrictInt] = Field(default=None, description="Положили в корзину, штук", alias="addToCartCount")
    orders_count: Optional[StrictInt] = Field(default=None, description="Заказали товаров, шт", alias="ordersCount")
    orders_sum_rub: Optional[StrictInt] = Field(default=None, description="Заказали на сумму, руб.", alias="ordersSumRub")
    buyouts_count: Optional[StrictInt] = Field(default=None, description="Выкупили товаров, шт.", alias="buyoutsCount")
    buyouts_sum_rub: Optional[StrictInt] = Field(default=None, description="Выкупили на сумму, руб.", alias="buyoutsSumRub")
    buyout_percent: Optional[StrictInt] = Field(default=None, description="Процент выкупа, % (Какой процент посетителей, заказавших товар, его выкупили. Без учёта товаров, которые еще доставляются покупателю.)", alias="buyoutPercent")
    add_to_cart_conversion: Optional[StrictInt] = Field(default=None, description="Конверсия в корзину, % (Какой процент посетителей, открывших карточку товара, добавили товар в корзину)", alias="addToCartConversion")
    cart_to_order_conversion: Optional[StrictInt] = Field(default=None, description="Конверсия в заказ, % (Какой процент посетителей, добавивших товар в корзину, сделали заказ)", alias="cartToOrderConversion")
    __properties: ClassVar[List[str]] = ["dt", "openCardCount", "addToCartCount", "ordersCount", "ordersSumRub", "buyoutsCount", "buyoutsSumRub", "buyoutPercent", "addToCartConversion", "cartToOrderConversion"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of NmReportGroupedHistoryResponseDataInnerHistoryInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NmReportGroupedHistoryResponseDataInnerHistoryInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dt": obj.get("dt"),
            "openCardCount": obj.get("openCardCount"),
            "addToCartCount": obj.get("addToCartCount"),
            "ordersCount": obj.get("ordersCount"),
            "ordersSumRub": obj.get("ordersSumRub"),
            "buyoutsCount": obj.get("buyoutsCount"),
            "buyoutsSumRub": obj.get("buyoutsSumRub"),
            "buyoutPercent": obj.get("buyoutPercent"),
            "addToCartConversion": obj.get("addToCartConversion"),
            "cartToOrderConversion": obj.get("cartToOrderConversion")
        })
        return _obj

