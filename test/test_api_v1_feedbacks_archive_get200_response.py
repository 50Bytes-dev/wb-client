# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.api_v1_feedbacks_archive_get200_response import ApiV1FeedbacksArchiveGet200Response

class TestApiV1FeedbacksArchiveGet200Response(unittest.TestCase):
    """ApiV1FeedbacksArchiveGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1FeedbacksArchiveGet200Response:
        """Test ApiV1FeedbacksArchiveGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1FeedbacksArchiveGet200Response`
        """
        model = ApiV1FeedbacksArchiveGet200Response()
        if include_optional:
            return ApiV1FeedbacksArchiveGet200Response(
                data = wildberries_async_api_client.models._api_v1_feedbacks_archive_get_200_response_data._api_v1_feedbacks_archive_get_200_response_data(
                    feedbacks = [
                        wildberries_async_api_client.models.response_feedback_inner.responseFeedback_inner(
                            id = '', 
                            user_name = '', 
                            matching_size = '', 
                            text = '', 
                            product_valuation = 56, 
                            created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            state = '', 
                            answer = wildberries_async_api_client.models.response_feedback_inner_answer.responseFeedback_inner_answer(
                                text = '', 
                                state = '', ), 
                            product_details = wildberries_async_api_client.models._api_v1_feedback_get_200_response_data_product_details._api_v1_feedback_get_200_response_data_productDetails(
                                nm_id = 56, 
                                imt_id = 56, 
                                product_name = '', 
                                supplier_article = '', 
                                supplier_name = '', 
                                brand_name = '', 
                                size = '', ), 
                            photo_links = [
                                wildberries_async_api_client.models._api_v1_feedback_get_200_response_data_photo_links_inner._api_v1_feedback_get_200_response_data_photoLinks_inner(
                                    full_size = '', 
                                    mini_size = '', )
                                ], 
                            video = wildberries_async_api_client.models._api_v1_feedback_get_200_response_data_video._api_v1_feedback_get_200_response_data_video(
                                preview_image = '', 
                                link = '', 
                                duration_sec = 56, ), 
                            was_viewed = True, 
                            is_able_supplier_feedback_valuation = True, 
                            supplier_feedback_valuation = 56, 
                            is_able_supplier_product_valuation = True, 
                            supplier_product_valuation = 56, 
                            is_able_return_product_orders = True, 
                            return_product_orders_date = '', 
                            bables = [
                                ''
                                ], )
                        ], ),
                error = True,
                error_text = '',
                additional_errors = [
                    ''
                    ]
            )
        else:
            return ApiV1FeedbacksArchiveGet200Response(
        )
        """

    def testApiV1FeedbacksArchiveGet200Response(self):
        """Test ApiV1FeedbacksArchiveGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()