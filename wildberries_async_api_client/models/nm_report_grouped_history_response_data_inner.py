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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from wildberries_async_api_client.models.nm_report_grouped_history_response_data_inner_history_inner import NmReportGroupedHistoryResponseDataInnerHistoryInner
from wildberries_async_api_client.models.nm_report_grouped_history_response_data_inner_object import NmReportGroupedHistoryResponseDataInnerObject
from wildberries_async_api_client.models.nm_report_grouped_history_response_data_inner_tag import NmReportGroupedHistoryResponseDataInnerTag
from typing import Optional, Set
from typing_extensions import Self

class NmReportGroupedHistoryResponseDataInner(BaseModel):
    """
    NmReportGroupedHistoryResponseDataInner
    """ # noqa: E501
    object: Optional[NmReportGroupedHistoryResponseDataInnerObject] = None
    brand_name: Optional[StrictStr] = Field(default=None, description="Название бренда", alias="brandName")
    tag: Optional[NmReportGroupedHistoryResponseDataInnerTag] = None
    history: Optional[List[NmReportGroupedHistoryResponseDataInnerHistoryInner]] = None
    __properties: ClassVar[List[str]] = ["object", "brandName", "tag", "history"]

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
        """Create an instance of NmReportGroupedHistoryResponseDataInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of object
        if self.object:
            _dict['object'] = self.object.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tag
        if self.tag:
            _dict['tag'] = self.tag.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in history (list)
        _items = []
        if self.history:
            for _item in self.history:
                if _item:
                    _items.append(_item.to_dict())
            _dict['history'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NmReportGroupedHistoryResponseDataInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": NmReportGroupedHistoryResponseDataInnerObject.from_dict(obj["object"]) if obj.get("object") is not None else None,
            "brandName": obj.get("brandName"),
            "tag": NmReportGroupedHistoryResponseDataInnerTag.from_dict(obj["tag"]) if obj.get("tag") is not None else None,
            "history": [NmReportGroupedHistoryResponseDataInnerHistoryInner.from_dict(_item) for _item in obj["history"]] if obj.get("history") is not None else None
        })
        return _obj

