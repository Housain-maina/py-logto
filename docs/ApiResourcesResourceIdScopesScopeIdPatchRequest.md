# ApiResourcesResourceIdScopesScopeIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The updated name of the scope. It should be unique for the resource. | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from py_logto.models.api_resources_resource_id_scopes_scope_id_patch_request import ApiResourcesResourceIdScopesScopeIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResourcesResourceIdScopesScopeIdPatchRequest from a JSON string
api_resources_resource_id_scopes_scope_id_patch_request_instance = ApiResourcesResourceIdScopesScopeIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(ApiResourcesResourceIdScopesScopeIdPatchRequest.to_json())

# convert the object into a dict
api_resources_resource_id_scopes_scope_id_patch_request_dict = api_resources_resource_id_scopes_scope_id_patch_request_instance.to_dict()
# create an instance of ApiResourcesResourceIdScopesScopeIdPatchRequest from a dict
api_resources_resource_id_scopes_scope_id_patch_request_from_dict = ApiResourcesResourceIdScopesScopeIdPatchRequest.from_dict(api_resources_resource_id_scopes_scope_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


