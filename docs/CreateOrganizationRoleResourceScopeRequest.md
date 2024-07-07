# CreateOrganizationRoleResourceScopeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope_ids** | **List[str]** | An array of resource scope IDs to be assigned. Existed scope IDs assignments will be ignored. | 

## Example

```python
from py_logto.models.create_organization_role_resource_scope_request import CreateOrganizationRoleResourceScopeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrganizationRoleResourceScopeRequest from a JSON string
create_organization_role_resource_scope_request_instance = CreateOrganizationRoleResourceScopeRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOrganizationRoleResourceScopeRequest.to_json())

# convert the object into a dict
create_organization_role_resource_scope_request_dict = create_organization_role_resource_scope_request_instance.to_dict()
# create an instance of CreateOrganizationRoleResourceScopeRequest from a dict
create_organization_role_resource_scope_request_from_dict = CreateOrganizationRoleResourceScopeRequest.from_dict(create_organization_role_resource_scope_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


