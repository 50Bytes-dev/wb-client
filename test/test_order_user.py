# coding: utf-8

"""
    Описание API Marketplace

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wb_client.models.order_user import OrderUser

class TestOrderUser(unittest.TestCase):
    """OrderUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderUser:
        """Test OrderUser
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderUser`
        """
        model = OrderUser()
        if include_optional:
            return OrderUser(
                fio = '',
                phone = ''
            )
        else:
            return OrderUser(
        )
        """

    def testOrderUser(self):
        """Test OrderUser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
