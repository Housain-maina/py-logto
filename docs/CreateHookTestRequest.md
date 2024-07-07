# CreateHookTestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | **List[str]** | An array of hook events for testing. | 
**config** | [**CreateHookTestRequestConfig**](CreateHookTestRequestConfig.md) |  | 
**event** | **object** | Use &#x60;events&#x60; instead. | [optional] 

## Example

```python
from py_logto.models.create_hook_test_request import CreateHookTestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHookTestRequest from a JSON string
create_hook_test_request_instance = CreateHookTestRequest.from_json(json)
# print the JSON string representation of the object
print(CreateHookTestRequest.to_json())

# convert the object into a dict
create_hook_test_request_dict = create_hook_test_request_instance.to_dict()
# create an instance of CreateHookTestRequest from a dict
create_hook_test_request_from_dict = CreateHookTestRequest.from_dict(create_hook_test_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


