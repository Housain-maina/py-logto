# ListRoleScopes200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**id** | **str** |  | 
**resource_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**created_at** | **float** |  | 
**resource** | [**GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource**](GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource.md) |  | 

## Example

```python
from py_logto.models.list_role_scopes200_response_inner import ListRoleScopes200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListRoleScopes200ResponseInner from a JSON string
list_role_scopes200_response_inner_instance = ListRoleScopes200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListRoleScopes200ResponseInner.to_json())

# convert the object into a dict
list_role_scopes200_response_inner_dict = list_role_scopes200_response_inner_instance.to_dict()
# create an instance of ListRoleScopes200ResponseInner from a dict
list_role_scopes200_response_inner_from_dict = ListRoleScopes200ResponseInner.from_dict(list_role_scopes200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


