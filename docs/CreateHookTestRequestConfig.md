# CreateHookTestRequestConfig

The hook configuration for testing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**headers** | **Dict[str, str]** |  | [optional] 
**retries** | **float** | Now the retry times is fixed to 3. Keep for backward compatibility. | [optional] 

## Example

```python
from py_logto.models.create_hook_test_request_config import CreateHookTestRequestConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHookTestRequestConfig from a JSON string
create_hook_test_request_config_instance = CreateHookTestRequestConfig.from_json(json)
# print the JSON string representation of the object
print(CreateHookTestRequestConfig.to_json())

# convert the object into a dict
create_hook_test_request_config_dict = create_hook_test_request_config_instance.to_dict()
# create an instance of CreateHookTestRequestConfig from a dict
create_hook_test_request_config_from_dict = CreateHookTestRequestConfig.from_dict(create_hook_test_request_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


