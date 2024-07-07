# AssignOrganizationRolesToApplicationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_ids** | **List[str]** | An array of application IDs to assign roles to. | 
**organization_role_ids** | **List[str]** | An array of organization role IDs to assign to the applications. | 

## Example

```python
from py_logto.models.assign_organization_roles_to_applications_request import AssignOrganizationRolesToApplicationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignOrganizationRolesToApplicationsRequest from a JSON string
assign_organization_roles_to_applications_request_instance = AssignOrganizationRolesToApplicationsRequest.from_json(json)
# print the JSON string representation of the object
print(AssignOrganizationRolesToApplicationsRequest.to_json())

# convert the object into a dict
assign_organization_roles_to_applications_request_dict = assign_organization_roles_to_applications_request_instance.to_dict()
# create an instance of AssignOrganizationRolesToApplicationsRequest from a dict
assign_organization_roles_to_applications_request_from_dict = AssignOrganizationRolesToApplicationsRequest.from_dict(assign_organization_roles_to_applications_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


