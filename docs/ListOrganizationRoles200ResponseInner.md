# ListOrganizationRoles200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**type** | **str** |  | 
**scopes** | [**List[ListApplicationOrganizations200ResponseInnerOrganizationRolesInner]**](ListApplicationOrganizations200ResponseInnerOrganizationRolesInner.md) |  | 
**resource_scopes** | [**List[ListOrganizationRoles200ResponseInnerResourceScopesInner]**](ListOrganizationRoles200ResponseInnerResourceScopesInner.md) |  | 

## Example

```python
from py_logto.models.list_organization_roles200_response_inner import ListOrganizationRoles200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListOrganizationRoles200ResponseInner from a JSON string
list_organization_roles200_response_inner_instance = ListOrganizationRoles200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListOrganizationRoles200ResponseInner.to_json())

# convert the object into a dict
list_organization_roles200_response_inner_dict = list_organization_roles200_response_inner_instance.to_dict()
# create an instance of ListOrganizationRoles200ResponseInner from a dict
list_organization_roles200_response_inner_from_dict = ListOrganizationRoles200ResponseInner.from_dict(list_organization_roles200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


