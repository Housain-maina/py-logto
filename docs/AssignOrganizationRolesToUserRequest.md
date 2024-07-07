# AssignOrganizationRolesToUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_role_ids** | **List[str]** | An array of organization role IDs to assign to the user. User existed roles assignment will be ignored. | 

## Example

```python
from py_logto.models.assign_organization_roles_to_user_request import AssignOrganizationRolesToUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignOrganizationRolesToUserRequest from a JSON string
assign_organization_roles_to_user_request_instance = AssignOrganizationRolesToUserRequest.from_json(json)
# print the JSON string representation of the object
print(AssignOrganizationRolesToUserRequest.to_json())

# convert the object into a dict
assign_organization_roles_to_user_request_dict = assign_organization_roles_to_user_request_instance.to_dict()
# create an instance of AssignOrganizationRolesToUserRequest from a dict
assign_organization_roles_to_user_request_from_dict = AssignOrganizationRolesToUserRequest.from_dict(assign_organization_roles_to_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


