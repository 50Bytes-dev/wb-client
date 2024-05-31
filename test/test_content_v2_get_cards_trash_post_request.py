# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.content_v2_get_cards_trash_post_request import ContentV2GetCardsTrashPostRequest

class TestContentV2GetCardsTrashPostRequest(unittest.TestCase):
    """ContentV2GetCardsTrashPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContentV2GetCardsTrashPostRequest:
        """Test ContentV2GetCardsTrashPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContentV2GetCardsTrashPostRequest`
        """
        model = ContentV2GetCardsTrashPostRequest()
        if include_optional:
            return ContentV2GetCardsTrashPostRequest(
                settings = wildberries_async_api_client.models._content_v2_get_cards_trash_post_request_settings._content_v2_get_cards_trash_post_request_settings(
                    sort = wildberries_async_api_client.models._content_v2_get_cards_trash_post_request_settings_sort._content_v2_get_cards_trash_post_request_settings_sort(
                        ascending = True, ), 
                    cursor = wildberries_async_api_client.models._content_v2_get_cards_trash_post_request_settings_cursor._content_v2_get_cards_trash_post_request_settings_cursor(
                        limit = 56, ), 
                    filter = wildberries_async_api_client.models._content_v2_get_cards_trash_post_request_settings_filter._content_v2_get_cards_trash_post_request_settings_filter(
                        text_search = '', ), )
            )
        else:
            return ContentV2GetCardsTrashPostRequest(
        )
        """

    def testContentV2GetCardsTrashPostRequest(self):
        """Test ContentV2GetCardsTrashPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()