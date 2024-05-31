# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.response429_daily import Response429Daily

class TestResponse429Daily(unittest.TestCase):
    """Response429Daily unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Response429Daily:
        """Test Response429Daily
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Response429Daily`
        """
        model = Response429Daily()
        if include_optional:
            return Response429Daily(
                data = [
                    None
                    ],
                error = True,
                error_text = 'Превышен лимит отчётов в сутки. Максимальное количество отчётов - 20',
                additional_errors = [
                    wildberries_async_api_client.models.response_error_additional_errors_inner.responseError_additionalErrors_inner(
                        field = '', 
                        description = '', )
                    ]
            )
        else:
            return Response429Daily(
        )
        """

    def testResponse429Daily(self):
        """Test Response429Daily"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()