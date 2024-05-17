# ApiHooksPostRequestConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**headers** | **Dict[str, str]** |  | [optional] 
**retries** | **float** | Now the retry times is fixed to 3. Keep for backward compatibility. | [optional] 

## Example

```python
from py_logto.models.api_hooks_post_request_config import ApiHooksPostRequestConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ApiHooksPostRequestConfig from a JSON string
api_hooks_post_request_config_instance = ApiHooksPostRequestConfig.from_json(json)
# print the JSON string representation of the object
print(ApiHooksPostRequestConfig.to_json())

# convert the object into a dict
api_hooks_post_request_config_dict = api_hooks_post_request_config_instance.to_dict()
# create an instance of ApiHooksPostRequestConfig from a dict
api_hooks_post_request_config_from_dict = ApiHooksPostRequestConfig.from_dict(api_hooks_post_request_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


