# NmReportDetailResponseDataCardsInnerStatisticsPeriodComparisonConversions

Конверсии

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_to_cart_percent** | **int** | Конверсия в корзину, % (Какой процент посетителей, открывших карточку товара, добавили товар в корзину) | [optional] 
**cart_to_order_percent** | **int** | Конверсия в заказ, % (Какой процент посетителей, добавивших товар в корзину, сделали заказ) | [optional] 
**buyouts_percent** | **int** | Процент выкупа, % (Какой процент посетителей, заказавших товар, его выкупили. Без учёта товаров, которые еще доставляются покупателю.) | [optional] 

## Example

```python
from wildberries_async_api_client.models.nm_report_detail_response_data_cards_inner_statistics_period_comparison_conversions import NmReportDetailResponseDataCardsInnerStatisticsPeriodComparisonConversions

# TODO update the JSON string below
json = "{}"
# create an instance of NmReportDetailResponseDataCardsInnerStatisticsPeriodComparisonConversions from a JSON string
nm_report_detail_response_data_cards_inner_statistics_period_comparison_conversions_instance = NmReportDetailResponseDataCardsInnerStatisticsPeriodComparisonConversions.from_json(json)
# print the JSON string representation of the object
print(NmReportDetailResponseDataCardsInnerStatisticsPeriodComparisonConversions.to_json())

# convert the object into a dict
nm_report_detail_response_data_cards_inner_statistics_period_comparison_conversions_dict = nm_report_detail_response_data_cards_inner_statistics_period_comparison_conversions_instance.to_dict()
# create an instance of NmReportDetailResponseDataCardsInnerStatisticsPeriodComparisonConversions from a dict
nm_report_detail_response_data_cards_inner_statistics_period_comparison_conversions_from_dict = NmReportDetailResponseDataCardsInnerStatisticsPeriodComparisonConversions.from_dict(nm_report_detail_response_data_cards_inner_statistics_period_comparison_conversions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

