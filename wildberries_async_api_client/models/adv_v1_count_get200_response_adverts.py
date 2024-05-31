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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class AdvV1CountGet200ResponseAdverts(BaseModel):
    """
    AdvV1CountGet200ResponseAdverts
    """ # noqa: E501
    type: Optional[StrictInt] = Field(default=None, description="<dl> <dt>Тип медиакампании:</dt> <dd><code>1</code> - размещение по дням</dd> <dd><code>2</code> - размещение по просмотрам</dd> </dl> ")
    status: Optional[StrictInt] = Field(default=None, description="<dl> <dt>Статус медиакампании:</dt>   <dd><code>1</code> - черновик</dd>   <dd><code>2</code> - модерация   <dd><code>3</code> - отклонено (с возможностью вернуть на модерацию)</dd>   <dd><code>4</code> - одобрено</dd>   <dd><code>5</code> - запланировано</dd>   <dd><code>6</code> - на показах</dd>   <dd><code>7</code> - завершено</dd>   <dd><code>8</code> - отказался</dd>   <dd><code>9</code> - приостановлена продавцом</dd>   <dd><code>10</code> - пауза по дневному лимиту</dd>   <dd><code>11</code> - пауза по расходу бюджета</dd> </dl> ")
    count: Optional[StrictInt] = Field(default=None, description="Количество медиакампаний")
    __properties: ClassVar[List[str]] = ["type", "status", "count"]

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
        """Create an instance of AdvV1CountGet200ResponseAdverts from a JSON string"""
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
        """Create an instance of AdvV1CountGet200ResponseAdverts from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "status": obj.get("status"),
            "count": obj.get("count")
        })
        return _obj

