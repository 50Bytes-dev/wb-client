# NmReportGroupedResponseDataGroupsInnerStatisticsPreviousPeriod

Статистика за предыдущие 30 дней

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begin** | **str** | Начало периода | [optional] 
**end** | **str** | Конец периода | [optional] 
**open_card_count** | **int** | Количество переходов в КТ | [optional] 
**add_to_cart_count** | **int** | Положили в корзину, штук | [optional] 
**orders_count** | **int** | Заказали товаров, штук | [optional] 
**orders_sum_rub** | **float** | Заказали на сумму, руб. | [optional] 
**buyouts_count** | **int** | Выкупили товаров, штук | [optional] 
**buyouts_sum_rub** | **float** | Выкупили на сумму, руб. | [optional] 
**cancel_count** | **int** | Отменили товаров, штук | [optional] 
**cancel_sum_rub** | **int** | Отменили на сумму, руб | [optional] 
**avg_price_rub** | **float** | Средняя цена, руб. | [optional] 
**avg_orders_count_per_day** | **float** | Среднее количество заказов в день, шт. | [optional] 
**conversions** | [**NmReportGroupedResponseDataGroupsInnerStatisticsPreviousPeriodConversions**](NmReportGroupedResponseDataGroupsInnerStatisticsPreviousPeriodConversions.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.nm_report_grouped_response_data_groups_inner_statistics_previous_period import NmReportGroupedResponseDataGroupsInnerStatisticsPreviousPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of NmReportGroupedResponseDataGroupsInnerStatisticsPreviousPeriod from a JSON string
nm_report_grouped_response_data_groups_inner_statistics_previous_period_instance = NmReportGroupedResponseDataGroupsInnerStatisticsPreviousPeriod.from_json(json)
# print the JSON string representation of the object
print(NmReportGroupedResponseDataGroupsInnerStatisticsPreviousPeriod.to_json())

# convert the object into a dict
nm_report_grouped_response_data_groups_inner_statistics_previous_period_dict = nm_report_grouped_response_data_groups_inner_statistics_previous_period_instance.to_dict()
# create an instance of NmReportGroupedResponseDataGroupsInnerStatisticsPreviousPeriod from a dict
nm_report_grouped_response_data_groups_inner_statistics_previous_period_from_dict = NmReportGroupedResponseDataGroupsInnerStatisticsPreviousPeriod.from_dict(nm_report_grouped_response_data_groups_inner_statistics_previous_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

