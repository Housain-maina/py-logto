# ApiHooksIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The updated name of the hook. | [optional] 
**event** | **str** | Use &#x60;events&#x60; instead. | [optional] 
**events** | **List[str]** | An array of updated hook events. | [optional] 
**config** | [**ApiHooksPostRequestConfig**](ApiHooksPostRequestConfig.md) |  | [optional] 
**enabled** | **bool** |  | [optional] 
**created_at** | **float** |  | [optional] 

## Example

```python
from py_logto.models.api_hooks_id_patch_request import ApiHooksIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiHooksIdPatchRequest from a JSON string
api_hooks_id_patch_request_instance = ApiHooksIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(ApiHooksIdPatchRequest.to_json())

# convert the object into a dict
api_hooks_id_patch_request_dict = api_hooks_id_patch_request_instance.to_dict()
# create an instance of ApiHooksIdPatchRequest from a dict
api_hooks_id_patch_request_from_dict = ApiHooksIdPatchRequest.from_dict(api_hooks_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


