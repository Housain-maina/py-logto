# AddOrganizationUsersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[str]** | An array of user IDs to be added to the organization. Organization existed users assignment will be ignored. | 

## Example

```python
from py_logto.models.add_organization_users_request import AddOrganizationUsersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddOrganizationUsersRequest from a JSON string
add_organization_users_request_instance = AddOrganizationUsersRequest.from_json(json)
# print the JSON string representation of the object
print(AddOrganizationUsersRequest.to_json())

# convert the object into a dict
add_organization_users_request_dict = add_organization_users_request_instance.to_dict()
# create an instance of AddOrganizationUsersRequest from a dict
add_organization_users_request_from_dict = AddOrganizationUsersRequest.from_dict(add_organization_users_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


