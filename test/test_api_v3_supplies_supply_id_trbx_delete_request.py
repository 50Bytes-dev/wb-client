# coding: utf-8

"""
    Описание API Marketplace

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wb_client.models.api_v3_supplies_supply_id_trbx_delete_request import ApiV3SuppliesSupplyIdTrbxDeleteRequest

class TestApiV3SuppliesSupplyIdTrbxDeleteRequest(unittest.TestCase):
    """ApiV3SuppliesSupplyIdTrbxDeleteRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV3SuppliesSupplyIdTrbxDeleteRequest:
        """Test ApiV3SuppliesSupplyIdTrbxDeleteRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV3SuppliesSupplyIdTrbxDeleteRequest`
        """
        model = ApiV3SuppliesSupplyIdTrbxDeleteRequest()
        if include_optional:
            return ApiV3SuppliesSupplyIdTrbxDeleteRequest(
                trbx_ids = [
                    'WB-TRBX-1234567'
                    ]
            )
        else:
            return ApiV3SuppliesSupplyIdTrbxDeleteRequest(
                trbx_ids = [
                    'WB-TRBX-1234567'
                    ],
        )
        """

    def testApiV3SuppliesSupplyIdTrbxDeleteRequest(self):
        """Test ApiV3SuppliesSupplyIdTrbxDeleteRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()