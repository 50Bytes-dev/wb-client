# Error


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Код ошибки | [optional] 
**message** | **str** | Описание ошибки | [optional] 
**data** | **object** | Дополнительные данные, обогащающие ошибку | [optional] 

## Example

```python
from wb_client.models.error import Error

# TODO update the JSON string below
json = "{}"
# create an instance of Error from a JSON string
error_instance = Error.from_json(json)
# print the JSON string representation of the object
print(Error.to_json())

# convert the object into a dict
error_dict = error_instance.to_dict()
# create an instance of Error from a dict
error_from_dict = Error.from_dict(error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

