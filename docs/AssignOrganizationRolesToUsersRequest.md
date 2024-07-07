# AssignOrganizationRolesToUsersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[str]** | An array of user IDs to assign roles. | 
**organization_role_ids** | **List[str]** | An array of organization role IDs to assign. User existed roles assignment will be ignored. | 

## Example

```python
from py_logto.models.assign_organization_roles_to_users_request import AssignOrganizationRolesToUsersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignOrganizationRolesToUsersRequest from a JSON string
assign_organization_roles_to_users_request_instance = AssignOrganizationRolesToUsersRequest.from_json(json)
# print the JSON string representation of the object
print(AssignOrganizationRolesToUsersRequest.to_json())

# convert the object into a dict
assign_organization_roles_to_users_request_dict = assign_organization_roles_to_users_request_instance.to_dict()
# create an instance of AssignOrganizationRolesToUsersRequest from a dict
assign_organization_roles_to_users_request_from_dict = AssignOrganizationRolesToUsersRequest.from_dict(assign_organization_roles_to_users_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


