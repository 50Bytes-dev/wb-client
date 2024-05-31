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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class AdvV1AdvertGet200ResponseExtended(BaseModel):
    """
    AdvV1AdvertGet200ResponseExtended
    """ # noqa: E501
    reason: Optional[StrictStr] = Field(default=None, description="Комментарий модератора (при наличии)")
    expenses: Optional[StrictInt] = Field(default=None, description="Затраты")
    var_from: Optional[datetime] = Field(default=None, description="Начало показов медиакампании", alias="from")
    to: Optional[datetime] = Field(default=None, description="Конец показов медиакампании")
    updated_at: Optional[datetime] = Field(default=None, description="Время изменения медиакампании")
    price: Optional[StrictInt] = Field(default=None, description="Стоимость размещения по дням (для типа 1)")
    budget: Optional[StrictInt] = Field(default=None, description="Остаток бюджета (для типа 2)")
    operation: Optional[StrictInt] = Field(default=None, description="Источник списания (1 - баланс, 2 - счет)")
    contract_id: Optional[StrictInt] = Field(default=None, description="Идентификатор контракта (для продавцов на контракте)")
    __properties: ClassVar[List[str]] = ["reason", "expenses", "from", "to", "updated_at", "price", "budget", "operation", "contract_id"]

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
        """Create an instance of AdvV1AdvertGet200ResponseExtended from a JSON string"""
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
        # set to None if reason (nullable) is None
        # and model_fields_set contains the field
        if self.reason is None and "reason" in self.model_fields_set:
            _dict['reason'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AdvV1AdvertGet200ResponseExtended from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "reason": obj.get("reason"),
            "expenses": obj.get("expenses"),
            "from": obj.get("from"),
            "to": obj.get("to"),
            "updated_at": obj.get("updated_at"),
            "price": obj.get("price"),
            "budget": obj.get("budget"),
            "operation": obj.get("operation"),
            "contract_id": obj.get("contract_id")
        })
        return _obj

