# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.content_v2_tag_id_patch400_response import ContentV2TagIdPatch400Response

class TestContentV2TagIdPatch400Response(unittest.TestCase):
    """ContentV2TagIdPatch400Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContentV2TagIdPatch400Response:
        """Test ContentV2TagIdPatch400Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContentV2TagIdPatch400Response`
        """
        model = ContentV2TagIdPatch400Response()
        if include_optional:
            return ContentV2TagIdPatch400Response(
                data = wildberries_async_api_client.models.data.data(),
                error = True,
                error_text = '',
                additional_errors = wildberries_async_api_client.models.response_content_error4_additional_errors.responseContentError4_additionalErrors(
                    description = '', )
            )
        else:
            return ContentV2TagIdPatch400Response(
        )
        """

    def testContentV2TagIdPatch400Response(self):
        """Test ContentV2TagIdPatch400Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()