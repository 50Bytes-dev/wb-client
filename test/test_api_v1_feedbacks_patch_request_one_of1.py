# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.api_v1_feedbacks_patch_request_one_of1 import ApiV1FeedbacksPatchRequestOneOf1

class TestApiV1FeedbacksPatchRequestOneOf1(unittest.TestCase):
    """ApiV1FeedbacksPatchRequestOneOf1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1FeedbacksPatchRequestOneOf1:
        """Test ApiV1FeedbacksPatchRequestOneOf1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1FeedbacksPatchRequestOneOf1`
        """
        model = ApiV1FeedbacksPatchRequestOneOf1()
        if include_optional:
            return ApiV1FeedbacksPatchRequestOneOf1(
                id = 'n5um6IUBQOOSTxXoo0gV',
                text = 'текст ответа'
            )
        else:
            return ApiV1FeedbacksPatchRequestOneOf1(
                id = 'n5um6IUBQOOSTxXoo0gV',
                text = 'текст ответа',
        )
        """

    def testApiV1FeedbacksPatchRequestOneOf1(self):
        """Test ApiV1FeedbacksPatchRequestOneOf1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()