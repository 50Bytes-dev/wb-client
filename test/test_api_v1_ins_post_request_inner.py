# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.api_v1_ins_post_request_inner import ApiV1InsPostRequestInner

class TestApiV1InsPostRequestInner(unittest.TestCase):
    """ApiV1InsPostRequestInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1InsPostRequestInner:
        """Test ApiV1InsPostRequestInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1InsPostRequestInner`
        """
        model = ApiV1InsPostRequestInner()
        if include_optional:
            return ApiV1InsPostRequestInner(
                nm = 56,
                recom = [
                    1
                    ]
            )
        else:
            return ApiV1InsPostRequestInner(
                nm = 56,
                recom = [
                    1
                    ],
        )
        """

    def testApiV1InsPostRequestInner(self):
        """Test ApiV1InsPostRequestInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()