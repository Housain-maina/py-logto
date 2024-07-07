# AssignOrganizationRolesToApplicationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_role_ids** | **List[str]** | The role ID to add. | 

## Example

```python
from py_logto.models.assign_organization_roles_to_application_request import AssignOrganizationRolesToApplicationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignOrganizationRolesToApplicationRequest from a JSON string
assign_organization_roles_to_application_request_instance = AssignOrganizationRolesToApplicationRequest.from_json(json)
# print the JSON string representation of the object
print(AssignOrganizationRolesToApplicationRequest.to_json())

# convert the object into a dict
assign_organization_roles_to_application_request_dict = assign_organization_roles_to_application_request_instance.to_dict()
# create an instance of AssignOrganizationRolesToApplicationRequest from a dict
assign_organization_roles_to_application_request_from_dict = AssignOrganizationRolesToApplicationRequest.from_dict(assign_organization_roles_to_application_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


