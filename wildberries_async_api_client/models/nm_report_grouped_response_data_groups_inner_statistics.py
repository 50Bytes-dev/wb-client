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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from wildberries_async_api_client.models.nm_report_grouped_response_data_groups_inner_statistics_period_comparison import NmReportGroupedResponseDataGroupsInnerStatisticsPeriodComparison
from wildberries_async_api_client.models.nm_report_grouped_response_data_groups_inner_statistics_previous_period import NmReportGroupedResponseDataGroupsInnerStatisticsPreviousPeriod
from wildberries_async_api_client.models.nm_report_grouped_response_data_groups_inner_statistics_selected_period import NmReportGroupedResponseDataGroupsInnerStatisticsSelectedPeriod
from typing import Optional, Set
from typing_extensions import Self

class NmReportGroupedResponseDataGroupsInnerStatistics(BaseModel):
    """
    NmReportGroupedResponseDataGroupsInnerStatistics
    """ # noqa: E501
    selected_period: Optional[NmReportGroupedResponseDataGroupsInnerStatisticsSelectedPeriod] = Field(default=None, alias="selectedPeriod")
    previous_period: Optional[NmReportGroupedResponseDataGroupsInnerStatisticsPreviousPeriod] = Field(default=None, alias="previousPeriod")
    period_comparison: Optional[NmReportGroupedResponseDataGroupsInnerStatisticsPeriodComparison] = Field(default=None, alias="periodComparison")
    __properties: ClassVar[List[str]] = ["selectedPeriod", "previousPeriod", "periodComparison"]

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
        """Create an instance of NmReportGroupedResponseDataGroupsInnerStatistics from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of selected_period
        if self.selected_period:
            _dict['selectedPeriod'] = self.selected_period.to_dict()
        # override the default output from pydantic by calling `to_dict()` of previous_period
        if self.previous_period:
            _dict['previousPeriod'] = self.previous_period.to_dict()
        # override the default output from pydantic by calling `to_dict()` of period_comparison
        if self.period_comparison:
            _dict['periodComparison'] = self.period_comparison.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NmReportGroupedResponseDataGroupsInnerStatistics from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "selectedPeriod": NmReportGroupedResponseDataGroupsInnerStatisticsSelectedPeriod.from_dict(obj["selectedPeriod"]) if obj.get("selectedPeriod") is not None else None,
            "previousPeriod": NmReportGroupedResponseDataGroupsInnerStatisticsPreviousPeriod.from_dict(obj["previousPeriod"]) if obj.get("previousPeriod") is not None else None,
            "periodComparison": NmReportGroupedResponseDataGroupsInnerStatisticsPeriodComparison.from_dict(obj["periodComparison"]) if obj.get("periodComparison") is not None else None
        })
        return _obj

