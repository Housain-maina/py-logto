# ApiHooksIdPatch200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**event** | **str** |  | 
**events** | **List[str]** |  | 
**config** | [**ApiHooksGet200ResponseInnerConfig**](ApiHooksGet200ResponseInnerConfig.md) |  | 
**signing_key** | **str** |  | 
**enabled** | **bool** |  | 
**created_at** | **float** |  | 

## Example

```python
from py_logto.models.api_hooks_id_patch200_response import ApiHooksIdPatch200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiHooksIdPatch200Response from a JSON string
api_hooks_id_patch200_response_instance = ApiHooksIdPatch200Response.from_json(json)
# print the JSON string representation of the object
print(ApiHooksIdPatch200Response.to_json())

# convert the object into a dict
api_hooks_id_patch200_response_dict = api_hooks_id_patch200_response_instance.to_dict()
# create an instance of ApiHooksIdPatch200Response from a dict
api_hooks_id_patch200_response_from_dict = ApiHooksIdPatch200Response.from_dict(api_hooks_id_patch200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


