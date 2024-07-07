# ReplaceOrganizationUserRolesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_role_ids** | **List[str]** | An array of organization role IDs to update for the user. | 

## Example

```python
from py_logto.models.replace_organization_user_roles_request import ReplaceOrganizationUserRolesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceOrganizationUserRolesRequest from a JSON string
replace_organization_user_roles_request_instance = ReplaceOrganizationUserRolesRequest.from_json(json)
# print the JSON string representation of the object
print(ReplaceOrganizationUserRolesRequest.to_json())

# convert the object into a dict
replace_organization_user_roles_request_dict = replace_organization_user_roles_request_instance.to_dict()
# create an instance of ReplaceOrganizationUserRolesRequest from a dict
replace_organization_user_roles_request_from_dict = ReplaceOrganizationUserRolesRequest.from_dict(replace_organization_user_roles_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


