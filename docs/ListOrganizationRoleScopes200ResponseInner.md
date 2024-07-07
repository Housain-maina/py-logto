# ListOrganizationRoleScopes200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 

## Example

```python
from py_logto.models.list_organization_role_scopes200_response_inner import ListOrganizationRoleScopes200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListOrganizationRoleScopes200ResponseInner from a JSON string
list_organization_role_scopes200_response_inner_instance = ListOrganizationRoleScopes200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListOrganizationRoleScopes200ResponseInner.to_json())

# convert the object into a dict
list_organization_role_scopes200_response_inner_dict = list_organization_role_scopes200_response_inner_instance.to_dict()
# create an instance of ListOrganizationRoleScopes200ResponseInner from a dict
list_organization_role_scopes200_response_inner_from_dict = ListOrganizationRoleScopes200ResponseInner.from_dict(list_organization_role_scopes200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


