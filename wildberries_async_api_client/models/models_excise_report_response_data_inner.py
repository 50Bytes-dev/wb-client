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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class ModelsExciseReportResponseDataInner(BaseModel):
    """
    ModelsExciseReportResponseDataInner
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="Страна покупателя")
    price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Цена товара, с НДС")
    currency_name_short: Optional[StrictStr] = Field(default=None, description="Валюта")
    excise_short: Optional[StrictStr] = Field(default=None, description="Код маркировки")
    barcode: Optional[StrictStr] = Field(default=None, description="Баркод")
    nm_id: Optional[StrictInt] = Field(default=None, description="Артикул Wildberries")
    operation_type_id: Optional[StrictInt] = Field(default=None, description="Тип операции, если есть:    * `1` — вывод из оборота   * `2` — возврат в оборот ")
    fiscal_doc_number: Optional[StrictInt] = Field(default=None, description="Номер фискального документа (чека полного расчёта), если есть")
    fiscal_dt: Optional[StrictStr] = Field(default=None, description="Дата фискализации (дата в чеке), если есть, `ГГГГ-ММ-ДД`")
    fiscal_drive_number: Optional[StrictStr] = Field(default=None, description="Номер фискального накопителя, если есть")
    rid: Optional[StrictInt] = Field(default=None, description="`Rid` ")
    srid: Optional[StrictStr] = Field(default=None, description="`Srid`  ")
    __properties: ClassVar[List[str]] = ["name", "price", "currency_name_short", "excise_short", "barcode", "nm_id", "operation_type_id", "fiscal_doc_number", "fiscal_dt", "fiscal_drive_number", "rid", "srid"]

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
        """Create an instance of ModelsExciseReportResponseDataInner from a JSON string"""
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
        """Create an instance of ModelsExciseReportResponseDataInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "price": obj.get("price"),
            "currency_name_short": obj.get("currency_name_short"),
            "excise_short": obj.get("excise_short"),
            "barcode": obj.get("barcode"),
            "nm_id": obj.get("nm_id"),
            "operation_type_id": obj.get("operation_type_id"),
            "fiscal_doc_number": obj.get("fiscal_doc_number"),
            "fiscal_dt": obj.get("fiscal_dt"),
            "fiscal_drive_number": obj.get("fiscal_drive_number"),
            "rid": obj.get("rid"),
            "srid": obj.get("srid")
        })
        return _obj

