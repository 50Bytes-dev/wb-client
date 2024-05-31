# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.content_v2_cards_error_list_get200_response import ContentV2CardsErrorListGet200Response

class TestContentV2CardsErrorListGet200Response(unittest.TestCase):
    """ContentV2CardsErrorListGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContentV2CardsErrorListGet200Response:
        """Test ContentV2CardsErrorListGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContentV2CardsErrorListGet200Response`
        """
        model = ContentV2CardsErrorListGet200Response()
        if include_optional:
            return ContentV2CardsErrorListGet200Response(
                data = [
                    wildberries_async_api_client.models._content_v2_cards_error_list_get_200_response_data_inner._content_v2_cards_error_list_get_200_response_data_inner(
                        object = 'Блузки', 
                        vendor_code = '6000000001', 
                        update_at = '2022-06-15T14:37:13Z', 
                        errors = [
                            'Поля Рос. размер, Размер обязательны для заполнения'
                            ], 
                        object_id = 41, )
                    ],
                error = False,
                error_text = '',
                additional_errors = ''
            )
        else:
            return ContentV2CardsErrorListGet200Response(
        )
        """

    def testContentV2CardsErrorListGet200Response(self):
        """Test ContentV2CardsErrorListGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()