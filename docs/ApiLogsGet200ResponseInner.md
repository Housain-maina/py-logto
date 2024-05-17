# ApiLogsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**key** | **str** |  | 
**payload** | [**ApiLogsGet200ResponseInnerPayload**](ApiLogsGet200ResponseInnerPayload.md) |  | 
**created_at** | **float** |  | 

## Example

```python
from py_logto.models.api_logs_get200_response_inner import ApiLogsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiLogsGet200ResponseInner from a JSON string
api_logs_get200_response_inner_instance = ApiLogsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ApiLogsGet200ResponseInner.to_json())

# convert the object into a dict
api_logs_get200_response_inner_dict = api_logs_get200_response_inner_instance.to_dict()
# create an instance of ApiLogsGet200ResponseInner from a dict
api_logs_get200_response_inner_from_dict = ApiLogsGet200ResponseInner.from_dict(api_logs_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


