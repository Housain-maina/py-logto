# ReplaceApplicationRolesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_ids** | **List[str]** | An array of API resource role IDs to update for the application. | 

## Example

```python
from py_logto.models.replace_application_roles_request import ReplaceApplicationRolesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceApplicationRolesRequest from a JSON string
replace_application_roles_request_instance = ReplaceApplicationRolesRequest.from_json(json)
# print the JSON string representation of the object
print(ReplaceApplicationRolesRequest.to_json())

# convert the object into a dict
replace_application_roles_request_dict = replace_application_roles_request_instance.to_dict()
# create an instance of ReplaceApplicationRolesRequest from a dict
replace_application_roles_request_from_dict = ReplaceApplicationRolesRequest.from_dict(replace_application_roles_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


