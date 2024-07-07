# UpdateHookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 
**name** | **str** | The updated name of the hook. | [optional] 
**event** | **str** | Use &#x60;events&#x60; instead. | [optional] 
**events** | **List[str]** | An array of updated hook events. | [optional] 
**config** | [**CreateHookRequestConfig**](CreateHookRequestConfig.md) |  | [optional] 
**enabled** | **bool** |  | [optional] 
**created_at** | **float** |  | [optional] 

## Example

```python
from py_logto.models.update_hook_request import UpdateHookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateHookRequest from a JSON string
update_hook_request_instance = UpdateHookRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateHookRequest.to_json())

# convert the object into a dict
update_hook_request_dict = update_hook_request_instance.to_dict()
# create an instance of UpdateHookRequest from a dict
update_hook_request_from_dict = UpdateHookRequest.from_dict(update_hook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


