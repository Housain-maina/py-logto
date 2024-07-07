# CreateHookRequestConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**headers** | **Dict[str, str]** |  | [optional] 
**retries** | **float** | Now the retry times is fixed to 3. Keep for backward compatibility. | [optional] 

## Example

```python
from py_logto.models.create_hook_request_config import CreateHookRequestConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHookRequestConfig from a JSON string
create_hook_request_config_instance = CreateHookRequestConfig.from_json(json)
# print the JSON string representation of the object
print(CreateHookRequestConfig.to_json())

# convert the object into a dict
create_hook_request_config_dict = create_hook_request_config_instance.to_dict()
# create an instance of CreateHookRequestConfig from a dict
create_hook_request_config_from_dict = CreateHookRequestConfig.from_dict(create_hook_request_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


