# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.request_move_nms_imt_disconn import RequestMoveNmsImtDisconn

class TestRequestMoveNmsImtDisconn(unittest.TestCase):
    """RequestMoveNmsImtDisconn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RequestMoveNmsImtDisconn:
        """Test RequestMoveNmsImtDisconn
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RequestMoveNmsImtDisconn`
        """
        model = RequestMoveNmsImtDisconn()
        if include_optional:
            return RequestMoveNmsImtDisconn(
                nm_ids = [837459235,828572090]
            )
        else:
            return RequestMoveNmsImtDisconn(
                nm_ids = [837459235,828572090],
        )
        """

    def testRequestMoveNmsImtDisconn(self):
        """Test RequestMoveNmsImtDisconn"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()