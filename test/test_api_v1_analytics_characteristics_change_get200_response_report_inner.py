# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.api_v1_analytics_characteristics_change_get200_response_report_inner import ApiV1AnalyticsCharacteristicsChangeGet200ResponseReportInner

class TestApiV1AnalyticsCharacteristicsChangeGet200ResponseReportInner(unittest.TestCase):
    """ApiV1AnalyticsCharacteristicsChangeGet200ResponseReportInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1AnalyticsCharacteristicsChangeGet200ResponseReportInner:
        """Test ApiV1AnalyticsCharacteristicsChangeGet200ResponseReportInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1AnalyticsCharacteristicsChangeGet200ResponseReportInner`
        """
        model = ApiV1AnalyticsCharacteristicsChangeGet200ResponseReportInner()
        if include_optional:
            return ApiV1AnalyticsCharacteristicsChangeGet200ResponseReportInner(
                amount = 56,
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                new_barcode = '',
                new_color = '',
                new_sa = '',
                new_shk_id = 56,
                new_size = '',
                nm_id = 56,
                old_barcode = '',
                old_color = '',
                old_sa = '',
                old_shk_id = 56,
                old_size = ''
            )
        else:
            return ApiV1AnalyticsCharacteristicsChangeGet200ResponseReportInner(
        )
        """

    def testApiV1AnalyticsCharacteristicsChangeGet200ResponseReportInner(self):
        """Test ApiV1AnalyticsCharacteristicsChangeGet200ResponseReportInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()