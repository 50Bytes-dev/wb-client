import json
from typing import *

import aiohttp

from ..api_config import APIConfig, HTTPException
from ..models import *


async def get_apiv1tariffscommission(
    locale: Optional[str] = None, api_config_override: Optional[APIConfig] = None
) -> Union[Commission, CommissionChina, CommissionTurkey, CommissionUzbekistan]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/v1/tariffs/commission"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"locale": locale}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "get",
            base_path + path,
            params=query_params,
        ) as inital_response:
            try:
                response = await inital_response.json()
            except aiohttp.ContentTypeError:
                response_text = await inital_response.text()
                raise HTTPException(inital_response.status, f"Invalid response from server: { response_text}")
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f"{ response }")

            return (
                Union[Commission, CommissionChina, CommissionTurkey, CommissionUzbekistan](**response)
                if response is not None
                else Union[Commission, CommissionChina, CommissionTurkey, CommissionUzbekistan]()
            )
