# ApiOrganizationsIdUsersPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[str]** | An array of user IDs to be added to the organization. Organization existed users assignment will be ignored. | 

## Example

```python
from py_logto.models.api_organizations_id_users_post_request import ApiOrganizationsIdUsersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOrganizationsIdUsersPostRequest from a JSON string
api_organizations_id_users_post_request_instance = ApiOrganizationsIdUsersPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiOrganizationsIdUsersPostRequest.to_json())

# convert the object into a dict
api_organizations_id_users_post_request_dict = api_organizations_id_users_post_request_instance.to_dict()
# create an instance of ApiOrganizationsIdUsersPostRequest from a dict
api_organizations_id_users_post_request_from_dict = ApiOrganizationsIdUsersPostRequest.from_dict(api_organizations_id_users_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


