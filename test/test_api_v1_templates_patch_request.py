# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.api_v1_templates_patch_request import ApiV1TemplatesPatchRequest

class TestApiV1TemplatesPatchRequest(unittest.TestCase):
    """ApiV1TemplatesPatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1TemplatesPatchRequest:
        """Test ApiV1TemplatesPatchRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1TemplatesPatchRequest`
        """
        model = ApiV1TemplatesPatchRequest()
        if include_optional:
            return ApiV1TemplatesPatchRequest(
                name = '',
                template_id = 56,
                text = ''
            )
        else:
            return ApiV1TemplatesPatchRequest(
                name = '',
                template_id = 56,
                text = '',
        )
        """

    def testApiV1TemplatesPatchRequest(self):
        """Test ApiV1TemplatesPatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()