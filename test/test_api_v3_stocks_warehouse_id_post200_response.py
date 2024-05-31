# coding: utf-8

"""
    Описание API Marketplace

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wb_client.models.api_v3_stocks_warehouse_id_post200_response import ApiV3StocksWarehouseIdPost200Response

class TestApiV3StocksWarehouseIdPost200Response(unittest.TestCase):
    """ApiV3StocksWarehouseIdPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV3StocksWarehouseIdPost200Response:
        """Test ApiV3StocksWarehouseIdPost200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV3StocksWarehouseIdPost200Response`
        """
        model = ApiV3StocksWarehouseIdPost200Response()
        if include_optional:
            return ApiV3StocksWarehouseIdPost200Response(
                stocks = [
                    wb_client.models._api_v3_stocks__warehouse_id__post_200_response_stocks_inner._api_v3_stocks__warehouseId__post_200_response_stocks_inner(
                        sku = 'BarcodeTest123', 
                        amount = 10, )
                    ]
            )
        else:
            return ApiV3StocksWarehouseIdPost200Response(
        )
        """

    def testApiV3StocksWarehouseIdPost200Response(self):
        """Test ApiV3StocksWarehouseIdPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
