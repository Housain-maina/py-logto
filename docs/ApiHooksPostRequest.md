# ApiHooksPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the hook. | [optional] 
**event** | **str** | Use &#x60;events&#x60; instead. | [optional] 
**events** | **List[str]** | An array of hook events. | [optional] 
**config** | [**ApiHooksPostRequestConfig**](ApiHooksPostRequestConfig.md) |  | 
**enabled** | **bool** |  | [optional] 
**created_at** | **float** |  | [optional] 

## Example

```python
from py_logto.models.api_hooks_post_request import ApiHooksPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiHooksPostRequest from a JSON string
api_hooks_post_request_instance = ApiHooksPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiHooksPostRequest.to_json())

# convert the object into a dict
api_hooks_post_request_dict = api_hooks_post_request_instance.to_dict()
# create an instance of ApiHooksPostRequest from a dict
api_hooks_post_request_from_dict = ApiHooksPostRequest.from_dict(api_hooks_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


