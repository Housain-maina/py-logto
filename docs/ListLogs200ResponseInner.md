# ListLogs200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**id** | **str** |  | 
**key** | **str** |  | 
**payload** | [**ListLogs200ResponseInnerPayload**](ListLogs200ResponseInnerPayload.md) |  | 
**created_at** | **float** |  | 

## Example

```python
from py_logto.models.list_logs200_response_inner import ListLogs200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListLogs200ResponseInner from a JSON string
list_logs200_response_inner_instance = ListLogs200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListLogs200ResponseInner.to_json())

# convert the object into a dict
list_logs200_response_inner_dict = list_logs200_response_inner_instance.to_dict()
# create an instance of ListLogs200ResponseInner from a dict
list_logs200_response_inner_from_dict = ListLogs200ResponseInner.from_dict(list_logs200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


