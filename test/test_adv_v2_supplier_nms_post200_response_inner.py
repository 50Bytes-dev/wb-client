# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.adv_v2_supplier_nms_post200_response_inner import AdvV2SupplierNmsPost200ResponseInner

class TestAdvV2SupplierNmsPost200ResponseInner(unittest.TestCase):
    """AdvV2SupplierNmsPost200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvV2SupplierNmsPost200ResponseInner:
        """Test AdvV2SupplierNmsPost200ResponseInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvV2SupplierNmsPost200ResponseInner`
        """
        model = AdvV2SupplierNmsPost200ResponseInner()
        if include_optional:
            return AdvV2SupplierNmsPost200ResponseInner(
                title = 'Плед',
                nm = 146168367,
                subject_id = 765
            )
        else:
            return AdvV2SupplierNmsPost200ResponseInner(
        )
        """

    def testAdvV2SupplierNmsPost200ResponseInner(self):
        """Test AdvV2SupplierNmsPost200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()