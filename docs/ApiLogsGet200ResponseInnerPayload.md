# ApiLogsGet200ResponseInnerPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**result** | **str** |  | 
**error** | [**ApiLogsGet200ResponseInnerPayloadError**](ApiLogsGet200ResponseInnerPayloadError.md) |  | [optional] 
**ip** | **str** |  | [optional] 
**user_agent** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**application_id** | **str** |  | [optional] 
**session_id** | **str** |  | [optional] 

## Example

```python
from py_logto.models.api_logs_get200_response_inner_payload import ApiLogsGet200ResponseInnerPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ApiLogsGet200ResponseInnerPayload from a JSON string
api_logs_get200_response_inner_payload_instance = ApiLogsGet200ResponseInnerPayload.from_json(json)
# print the JSON string representation of the object
print(ApiLogsGet200ResponseInnerPayload.to_json())

# convert the object into a dict
api_logs_get200_response_inner_payload_dict = api_logs_get200_response_inner_payload_instance.to_dict()
# create an instance of ApiLogsGet200ResponseInnerPayload from a dict
api_logs_get200_response_inner_payload_from_dict = ApiLogsGet200ResponseInnerPayload.from_dict(api_logs_get200_response_inner_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


