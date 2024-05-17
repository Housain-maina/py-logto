# ApiHooksIdTestPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | **List[str]** | An array of hook events for testing. | 
**config** | [**ApiHooksIdTestPostRequestConfig**](ApiHooksIdTestPostRequestConfig.md) |  | 
**event** | **object** | Use &#x60;events&#x60; instead. | [optional] 

## Example

```python
from py_logto.models.api_hooks_id_test_post_request import ApiHooksIdTestPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiHooksIdTestPostRequest from a JSON string
api_hooks_id_test_post_request_instance = ApiHooksIdTestPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiHooksIdTestPostRequest.to_json())

# convert the object into a dict
api_hooks_id_test_post_request_dict = api_hooks_id_test_post_request_instance.to_dict()
# create an instance of ApiHooksIdTestPostRequest from a dict
api_hooks_id_test_post_request_from_dict = ApiHooksIdTestPostRequest.from_dict(api_hooks_id_test_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


