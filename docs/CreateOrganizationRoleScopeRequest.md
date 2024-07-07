# CreateOrganizationRoleScopeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_scope_ids** | **List[str]** | An array of organization scope IDs to be assigned. Existed scope IDs assignments will be ignored. | 

## Example

```python
from py_logto.models.create_organization_role_scope_request import CreateOrganizationRoleScopeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrganizationRoleScopeRequest from a JSON string
create_organization_role_scope_request_instance = CreateOrganizationRoleScopeRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOrganizationRoleScopeRequest.to_json())

# convert the object into a dict
create_organization_role_scope_request_dict = create_organization_role_scope_request_instance.to_dict()
# create an instance of CreateOrganizationRoleScopeRequest from a dict
create_organization_role_scope_request_from_dict = CreateOrganizationRoleScopeRequest.from_dict(create_organization_role_scope_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


