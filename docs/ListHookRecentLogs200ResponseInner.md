# ListHookRecentLogs200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**key** | **str** |  | 
**payload** | [**ListLogs200ResponseInnerPayload**](ListLogs200ResponseInnerPayload.md) |  | 
**created_at** | **float** |  | 

## Example

```python
from py_logto.models.list_hook_recent_logs200_response_inner import ListHookRecentLogs200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListHookRecentLogs200ResponseInner from a JSON string
list_hook_recent_logs200_response_inner_instance = ListHookRecentLogs200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListHookRecentLogs200ResponseInner.to_json())

# convert the object into a dict
list_hook_recent_logs200_response_inner_dict = list_hook_recent_logs200_response_inner_instance.to_dict()
# create an instance of ListHookRecentLogs200ResponseInner from a dict
list_hook_recent_logs200_response_inner_from_dict = ListHookRecentLogs200ResponseInner.from_dict(list_hook_recent_logs200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


