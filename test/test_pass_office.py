# coding: utf-8

"""
    Описание API Marketplace

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wb_client.models.pass_office import PassOffice

class TestPassOffice(unittest.TestCase):
    """PassOffice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PassOffice:
        """Test PassOffice
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PassOffice`
        """
        model = PassOffice()
        if include_optional:
            return PassOffice(
                name = 'Коледино',
                address = 'г. Подольск, д. Коледино, ул. Троицкая',
                id = 1
            )
        else:
            return PassOffice(
        )
        """

    def testPassOffice(self):
        """Test PassOffice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()