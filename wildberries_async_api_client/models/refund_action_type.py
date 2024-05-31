# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class RefundActionType(str, Enum):
    """
    Действие продавца по возврату:  - `sellerRequestRefund` — продавец запросил возврат товара  - `sellerRejectRefund` — продавец отклонил возврат товара  - `sellerAcceptFullRefund` — продавец одобрил возврат товара  - `sellerAcceptRefundInOffice` — продавец одобрил возврат товара на ПВЗ  
    """

    """
    allowed enum values
    """
    SELLERREQUESTREFUND = 'sellerRequestRefund'
    SELLERREJECTREFUND = 'sellerRejectRefund'
    SELLERACCEPTFULLREFUND = 'sellerAcceptFullRefund'
    SELLERACCEPTREFUNDINOFFICE = 'sellerAcceptRefundInOffice'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RefundActionType from a JSON string"""
        return cls(json.loads(json_str))

