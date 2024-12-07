# ListLogs200ResponseInnerPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**result** | **str** |  | 
**error** | [**ListLogs200ResponseInnerPayloadError**](ListLogs200ResponseInnerPayloadError.md) |  | [optional] 
**ip** | **str** |  | [optional] 
**user_agent** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**application_id** | **str** |  | [optional] 
**session_id** | **str** |  | [optional] 
**params** | **Dict[str, object]** |  | [optional] 

## Example

```python
from py_logto.models.list_logs200_response_inner_payload import ListLogs200ResponseInnerPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ListLogs200ResponseInnerPayload from a JSON string
list_logs200_response_inner_payload_instance = ListLogs200ResponseInnerPayload.from_json(json)
# print the JSON string representation of the object
print(ListLogs200ResponseInnerPayload.to_json())

# convert the object into a dict
list_logs200_response_inner_payload_dict = list_logs200_response_inner_payload_instance.to_dict()
# create an instance of ListLogs200ResponseInnerPayload from a dict
list_logs200_response_inner_payload_from_dict = ListLogs200ResponseInnerPayload.from_dict(list_logs200_response_inner_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


