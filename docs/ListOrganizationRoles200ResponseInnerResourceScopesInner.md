# ListOrganizationRoles200ResponseInnerResourceScopesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**resource** | [**ListApplicationOrganizations200ResponseInnerOrganizationRolesInner**](ListApplicationOrganizations200ResponseInnerOrganizationRolesInner.md) |  | 

## Example

```python
from py_logto.models.list_organization_roles200_response_inner_resource_scopes_inner import ListOrganizationRoles200ResponseInnerResourceScopesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListOrganizationRoles200ResponseInnerResourceScopesInner from a JSON string
list_organization_roles200_response_inner_resource_scopes_inner_instance = ListOrganizationRoles200ResponseInnerResourceScopesInner.from_json(json)
# print the JSON string representation of the object
print(ListOrganizationRoles200ResponseInnerResourceScopesInner.to_json())

# convert the object into a dict
list_organization_roles200_response_inner_resource_scopes_inner_dict = list_organization_roles200_response_inner_resource_scopes_inner_instance.to_dict()
# create an instance of ListOrganizationRoles200ResponseInnerResourceScopesInner from a dict
list_organization_roles200_response_inner_resource_scopes_inner_from_dict = ListOrganizationRoles200ResponseInnerResourceScopesInner.from_dict(list_organization_roles200_response_inner_resource_scopes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


