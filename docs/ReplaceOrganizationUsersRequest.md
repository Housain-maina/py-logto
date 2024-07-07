# ReplaceOrganizationUsersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[str]** | An array of user IDs to replace existing users. | 

## Example

```python
from py_logto.models.replace_organization_users_request import ReplaceOrganizationUsersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceOrganizationUsersRequest from a JSON string
replace_organization_users_request_instance = ReplaceOrganizationUsersRequest.from_json(json)
# print the JSON string representation of the object
print(ReplaceOrganizationUsersRequest.to_json())

# convert the object into a dict
replace_organization_users_request_dict = replace_organization_users_request_instance.to_dict()
# create an instance of ReplaceOrganizationUsersRequest from a dict
replace_organization_users_request_from_dict = ReplaceOrganizationUsersRequest.from_dict(replace_organization_users_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


