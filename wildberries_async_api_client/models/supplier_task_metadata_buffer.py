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

class SupplierTaskMetadataBuffer(BaseModel):
    """
    SupplierTaskMetadataBuffer
    """ # noqa: E501
    upload_id: Optional[StrictInt] = Field(default=None, description="ID загрузки", alias="uploadID")
    status: Optional[StrictInt] = Field(default=None, description="Статус загрузки: `1` — в обработке ")
    upload_date: Optional[date] = Field(default=None, description="Дата и время, когда загрузка создана", alias="uploadDate")
    activation_date: Optional[date] = Field(default=None, description="Дата и время, когда загрузка отправляется в обработку", alias="activationDate")
    over_all_goods_number: Optional[StrictInt] = Field(default=None, description="Всего товаров", alias="overAllGoodsNumber")
    success_goods_number: Optional[StrictInt] = Field(default=None, description="Товаров без ошибок (0, потому что загрузка в обработке)", alias="successGoodsNumber")
    __properties: ClassVar[List[str]] = ["uploadID", "status", "uploadDate", "activationDate", "overAllGoodsNumber", "successGoodsNumber"]

    @field_validator('upload_date')
    def upload_date_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"YYYY-MM-DDTHH:MM:SSZ", value):
            raise ValueError(r"must validate the regular expression /YYYY-MM-DDTHH:MM:SSZ/")
        return value

    @field_validator('activation_date')
    def activation_date_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"YYYY-MM-DDTHH:MM:SSZ", value):
            raise ValueError(r"must validate the regular expression /YYYY-MM-DDTHH:MM:SSZ/")
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
        """Create an instance of SupplierTaskMetadataBuffer from a JSON string"""
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
        """Create an instance of SupplierTaskMetadataBuffer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uploadID": obj.get("uploadID"),
            "status": obj.get("status"),
            "uploadDate": obj.get("uploadDate"),
            "activationDate": obj.get("activationDate"),
            "overAllGoodsNumber": obj.get("overAllGoodsNumber"),
            "successGoodsNumber": obj.get("successGoodsNumber")
        })
        return _obj

