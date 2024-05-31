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


class Sender(str, Enum):
    """
    Отправитель:  - `client` — покупатель  - `seller` — продавец   - `wb` — Wildberries  
    """

    """
    allowed enum values
    """
    CLIENT = 'client'
    SELLER = 'seller'
    WB = 'wb'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Sender from a JSON string"""
        return cls(json.loads(json_str))

