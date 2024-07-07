# ReplaceOrganizationApplicationRolesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_role_ids** | **List[str]** | An array of role IDs to replace existing roles. | 

## Example

```python
from py_logto.models.replace_organization_application_roles_request import ReplaceOrganizationApplicationRolesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceOrganizationApplicationRolesRequest from a JSON string
replace_organization_application_roles_request_instance = ReplaceOrganizationApplicationRolesRequest.from_json(json)
# print the JSON string representation of the object
print(ReplaceOrganizationApplicationRolesRequest.to_json())

# convert the object into a dict
replace_organization_application_roles_request_dict = replace_organization_application_roles_request_instance.to_dict()
# create an instance of ReplaceOrganizationApplicationRolesRequest from a dict
replace_organization_application_roles_request_from_dict = ReplaceOrganizationApplicationRolesRequest.from_dict(replace_organization_application_roles_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


