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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ModelPass(BaseModel):
    """
    Данные о пропуске продавца
    """ # noqa: E501
    first_name: Optional[StrictStr] = Field(default=None, description="Имя водителя", alias="firstName")
    date_end: Optional[StrictStr] = Field(default=None, description="Дата окончания действия пропуска", alias="dateEnd")
    last_name: Optional[StrictStr] = Field(default=None, description="Фамилия водителя", alias="lastName")
    car_model: Optional[StrictStr] = Field(default=None, description="Марка машины", alias="carModel")
    car_number: Optional[StrictStr] = Field(default=None, description="Номер машины", alias="carNumber")
    office_name: Optional[StrictStr] = Field(default=None, description="Название склада", alias="officeName")
    office_address: Optional[StrictStr] = Field(default=None, description="Адрес склада", alias="officeAddress")
    office_id: Optional[StrictInt] = Field(default=None, description="ID склада", alias="officeId")
    id: Optional[StrictInt] = Field(default=None, description="ID пропуска")
    __properties: ClassVar[List[str]] = ["firstName", "dateEnd", "lastName", "carModel", "carNumber", "officeName", "officeAddress", "officeId", "id"]

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
        """Create an instance of ModelPass from a JSON string"""
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
        """Create an instance of ModelPass from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "firstName": obj.get("firstName"),
            "dateEnd": obj.get("dateEnd"),
            "lastName": obj.get("lastName"),
            "carModel": obj.get("carModel"),
            "carNumber": obj.get("carNumber"),
            "officeName": obj.get("officeName"),
            "officeAddress": obj.get("officeAddress"),
            "officeId": obj.get("officeId"),
            "id": obj.get("id")
        })
        return _obj


