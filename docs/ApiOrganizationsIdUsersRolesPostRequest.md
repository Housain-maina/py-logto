# ApiOrganizationsIdUsersRolesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[str]** | An array of user IDs to assign roles. | 
**organization_role_ids** | **List[str]** | An array of organization role IDs to assign. User existed roles assignment will be ignored. | 

## Example

```python
from py_logto.models.api_organizations_id_users_roles_post_request import ApiOrganizationsIdUsersRolesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOrganizationsIdUsersRolesPostRequest from a JSON string
api_organizations_id_users_roles_post_request_instance = ApiOrganizationsIdUsersRolesPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiOrganizationsIdUsersRolesPostRequest.to_json())

# convert the object into a dict
api_organizations_id_users_roles_post_request_dict = api_organizations_id_users_roles_post_request_instance.to_dict()
# create an instance of ApiOrganizationsIdUsersRolesPostRequest from a dict
api_organizations_id_users_roles_post_request_from_dict = ApiOrganizationsIdUsersRolesPostRequest.from_dict(api_organizations_id_users_roles_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


