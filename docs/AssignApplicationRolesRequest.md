# AssignApplicationRolesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_ids** | **List[str]** | An array of API resource role IDs to assign. | 

## Example

```python
from py_logto.models.assign_application_roles_request import AssignApplicationRolesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignApplicationRolesRequest from a JSON string
assign_application_roles_request_instance = AssignApplicationRolesRequest.from_json(json)
# print the JSON string representation of the object
print(AssignApplicationRolesRequest.to_json())

# convert the object into a dict
assign_application_roles_request_dict = assign_application_roles_request_instance.to_dict()
# create an instance of AssignApplicationRolesRequest from a dict
assign_application_roles_request_from_dict = AssignApplicationRolesRequest.from_dict(assign_application_roles_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


