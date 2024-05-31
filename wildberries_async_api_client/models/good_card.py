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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class GoodCard(BaseModel):
    """
    Информация о заказе
    """ # noqa: E501
    var_date: Optional[StrictStr] = Field(default=None, description="Дата заказа", alias="date")
    need_refund: Optional[StrictBool] = Field(default=None, description="Запрошен ли возврат товара:  - `false` — не запрошен - `true` — запрошен ", alias="needRefund")
    nm_id: Optional[StrictInt] = Field(default=None, description="Артикул WB", alias="nmID")
    price: Optional[StrictInt] = Field(default=None, description="Стоимость заказа")
    price_currency: Optional[StrictStr] = Field(default=None, description="Валюта", alias="priceCurrency")
    rid: Optional[StrictStr] = Field(default=None, description="Уникальный ID заказа в WB")
    size: Optional[StrictStr] = Field(default=None, description="Размер товара")
    status_id: Optional[StrictInt] = Field(default=None, description="Статус товара: - `0` — Товар активный - `1` — Товар оформлен - `2` — Товар собирается  - `3` — Товар в пути - `4` — Товар ожидает в ПВЗ  - `5` — Товар у курьера - `10` — Товар в архиве  - `11` — Товар выкуплен  - `12` — Товар отменён  - `13` — Оформлен возврат  - `14` — Товар отменён (нет на складе) ", alias="statusID")
    __properties: ClassVar[List[str]] = ["date", "needRefund", "nmID", "price", "priceCurrency", "rid", "size", "statusID"]

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
        """Create an instance of GoodCard from a JSON string"""
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
        """Create an instance of GoodCard from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "date": obj.get("date"),
            "needRefund": obj.get("needRefund"),
            "nmID": obj.get("nmID"),
            "price": obj.get("price"),
            "priceCurrency": obj.get("priceCurrency"),
            "rid": obj.get("rid"),
            "size": obj.get("size"),
            "statusID": obj.get("statusID")
        })
        return _obj

