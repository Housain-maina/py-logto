# ReplaceOrganizationRoleResourceScopesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope_ids** | **List[str]** | An array of resource scope IDs to replace existing scopes. | 

## Example

```python
from py_logto.models.replace_organization_role_resource_scopes_request import ReplaceOrganizationRoleResourceScopesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceOrganizationRoleResourceScopesRequest from a JSON string
replace_organization_role_resource_scopes_request_instance = ReplaceOrganizationRoleResourceScopesRequest.from_json(json)
# print the JSON string representation of the object
print(ReplaceOrganizationRoleResourceScopesRequest.to_json())

# convert the object into a dict
replace_organization_role_resource_scopes_request_dict = replace_organization_role_resource_scopes_request_instance.to_dict()
# create an instance of ReplaceOrganizationRoleResourceScopesRequest from a dict
replace_organization_role_resource_scopes_request_from_dict = ReplaceOrganizationRoleResourceScopesRequest.from_dict(replace_organization_role_resource_scopes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


