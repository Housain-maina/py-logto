# ApiRolesIdScopesGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**resource_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**created_at** | **float** |  | 
**resource** | [**ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource**](ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource.md) |  | 

## Example

```python
from py_logto.models.api_roles_id_scopes_get200_response_inner import ApiRolesIdScopesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiRolesIdScopesGet200ResponseInner from a JSON string
api_roles_id_scopes_get200_response_inner_instance = ApiRolesIdScopesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ApiRolesIdScopesGet200ResponseInner.to_json())

# convert the object into a dict
api_roles_id_scopes_get200_response_inner_dict = api_roles_id_scopes_get200_response_inner_instance.to_dict()
# create an instance of ApiRolesIdScopesGet200ResponseInner from a dict
api_roles_id_scopes_get200_response_inner_from_dict = ApiRolesIdScopesGet200ResponseInner.from_dict(api_roles_id_scopes_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


