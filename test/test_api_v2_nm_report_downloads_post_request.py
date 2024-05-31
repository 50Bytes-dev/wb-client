# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.api_v2_nm_report_downloads_post_request import ApiV2NmReportDownloadsPostRequest

class TestApiV2NmReportDownloadsPostRequest(unittest.TestCase):
    """ApiV2NmReportDownloadsPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV2NmReportDownloadsPostRequest:
        """Test ApiV2NmReportDownloadsPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV2NmReportDownloadsPostRequest`
        """
        model = ApiV2NmReportDownloadsPostRequest()
        if include_optional:
            return ApiV2NmReportDownloadsPostRequest(
                id = '',
                report_type = '',
                user_report_name = '',
                params = wildberries_async_api_client.models.grouped_by_objects_brands_and_tags_req_params.GroupedByObjectsBrandsAndTagsReq_params(
                    subject_ids = [
                        56
                        ], 
                    brand_names = [
                        ''
                        ], 
                    tag_ids = [
                        56
                        ], 
                    start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    timezone = '', 
                    aggregation_level = '', 
                    skip_deleted_nm = True, )
            )
        else:
            return ApiV2NmReportDownloadsPostRequest(
                id = '',
                report_type = '',
        )
        """

    def testApiV2NmReportDownloadsPostRequest(self):
        """Test ApiV2NmReportDownloadsPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()