# CreateHookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 
**name** | **str** | The name of the hook. | [optional] 
**event** | **str** | Use &#x60;events&#x60; instead. | [optional] 
**events** | **List[str]** | An array of hook events. | [optional] 
**config** | [**CreateHookRequestConfig**](CreateHookRequestConfig.md) |  | 
**enabled** | **bool** |  | [optional] 
**created_at** | **float** |  | [optional] 

## Example

```python
from py_logto.models.create_hook_request import CreateHookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHookRequest from a JSON string
create_hook_request_instance = CreateHookRequest.from_json(json)
# print the JSON string representation of the object
print(CreateHookRequest.to_json())

# convert the object into a dict
create_hook_request_dict = create_hook_request_instance.to_dict()
# create an instance of CreateHookRequest from a dict
create_hook_request_from_dict = CreateHookRequest.from_dict(create_hook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


