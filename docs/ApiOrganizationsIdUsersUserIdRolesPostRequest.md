# ApiOrganizationsIdUsersUserIdRolesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_role_ids** | **List[str]** | An array of organization role IDs to assign to the user. User existed roles assignment will be ignored. | 

## Example

```python
from py_logto.models.api_organizations_id_users_user_id_roles_post_request import ApiOrganizationsIdUsersUserIdRolesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOrganizationsIdUsersUserIdRolesPostRequest from a JSON string
api_organizations_id_users_user_id_roles_post_request_instance = ApiOrganizationsIdUsersUserIdRolesPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiOrganizationsIdUsersUserIdRolesPostRequest.to_json())

# convert the object into a dict
api_organizations_id_users_user_id_roles_post_request_dict = api_organizations_id_users_user_id_roles_post_request_instance.to_dict()
# create an instance of ApiOrganizationsIdUsersUserIdRolesPostRequest from a dict
api_organizations_id_users_user_id_roles_post_request_from_dict = ApiOrganizationsIdUsersUserIdRolesPostRequest.from_dict(api_organizations_id_users_user_id_roles_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


