# coding: utf-8

"""
    Описание API Marketplace

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from wb_client.models.order_user import OrderUser
from typing import Optional, Set
from typing_extensions import Self

class SupplyOrder(BaseModel):
    """
    SupplyOrder
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Идентификатор сборочного задания в Маркетплейсе")
    rid: Optional[StrictStr] = Field(default=None, description="Идентификатор сборочного задания в системе Wildberries")
    created_at: Optional[datetime] = Field(default=None, description="Дата создания сборочного задания (RFC3339)", alias="createdAt")
    warehouse_id: Optional[StrictInt] = Field(default=None, description="Идентификатор склада продавца, на который поступило сборочное задание", alias="warehouseId")
    offices: Optional[List[StrictStr]] = Field(default=None, description="Список офисов, куда следует привезти товар")
    user: Optional[OrderUser] = None
    skus: Optional[List[StrictStr]] = Field(default=None, description="Массив баркодов товара")
    price: Optional[StrictInt] = Field(default=None, description="Цена в валюте продажи с учетом всех скидок, умноженная на 100. Код валюты продажи в поле currencyCode.")
    converted_price: Optional[StrictInt] = Field(default=None, description="Цена в валюте страны продавца с учетом всех скидок, кроме суммы по WB Кошельку, умноженная на 100. Предоставляется в информационных целях.", alias="convertedPrice")
    currency_code: Optional[StrictInt] = Field(default=None, description="Код валюты продажи (ISO 4217)", alias="currencyCode")
    converted_currency_code: Optional[StrictInt] = Field(default=None, description="Код валюты страны продавца (ISO 4217)", alias="convertedCurrencyCode")
    order_uid: Optional[StrictStr] = Field(default=None, description="Идентификатор транзакции для группировки сборочных заданий. Сборочные задания в одной корзине покупателя будут иметь одинаковый orderUID", alias="orderUid")
    nm_id: Optional[StrictInt] = Field(default=None, description="Артикул WB", alias="nmId")
    chrt_id: Optional[StrictInt] = Field(default=None, description="Идентификатор размера товара в системе Wildberries", alias="chrtId")
    article: Optional[StrictStr] = Field(default=None, description="Артикул продавца")
    color_code: Optional[StrictStr] = Field(default=None, description="Код цвета (только для колеруемых товаров)", alias="colorCode")
    cargo_type: Optional[StrictInt] = Field(default=None, description="<dl> <dt>Тип товара:</dt> <dd>1 - обычный</dd> <dd>2 - СГТ (Сверхгабаритный товар)</dd> <dd>3 - КГТ (Крупногабаритный товар). Не используется на данный момент.</dd> </dl> ", alias="cargoType")
    __properties: ClassVar[List[str]] = ["id", "rid", "createdAt", "warehouseId", "offices", "user", "skus", "price", "convertedPrice", "currencyCode", "convertedCurrencyCode", "orderUid", "nmId", "chrtId", "article", "colorCode", "cargoType"]

    @field_validator('cargo_type')
    def cargo_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([1, 2, 3]):
            raise ValueError("must be one of enum values (1, 2, 3)")
        return value

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
        """Create an instance of SupplyOrder from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # set to None if offices (nullable) is None
        # and model_fields_set contains the field
        if self.offices is None and "offices" in self.model_fields_set:
            _dict['offices'] = None

        # set to None if user (nullable) is None
        # and model_fields_set contains the field
        if self.user is None and "user" in self.model_fields_set:
            _dict['user'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SupplyOrder from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "rid": obj.get("rid"),
            "createdAt": obj.get("createdAt"),
            "warehouseId": obj.get("warehouseId"),
            "offices": obj.get("offices"),
            "user": OrderUser.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "skus": obj.get("skus"),
            "price": obj.get("price"),
            "convertedPrice": obj.get("convertedPrice"),
            "currencyCode": obj.get("currencyCode"),
            "convertedCurrencyCode": obj.get("convertedCurrencyCode"),
            "orderUid": obj.get("orderUid"),
            "nmId": obj.get("nmId"),
            "chrtId": obj.get("chrtId"),
            "article": obj.get("article"),
            "colorCode": obj.get("colorCode"),
            "cargoType": obj.get("cargoType")
        })
        return _obj


