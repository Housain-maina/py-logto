# ApiOrganizationsIdUsersUserIdRolesPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_role_ids** | **List[str]** | An array of organization role IDs to update for the user. | 

## Example

```python
from py_logto.models.api_organizations_id_users_user_id_roles_put_request import ApiOrganizationsIdUsersUserIdRolesPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOrganizationsIdUsersUserIdRolesPutRequest from a JSON string
api_organizations_id_users_user_id_roles_put_request_instance = ApiOrganizationsIdUsersUserIdRolesPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiOrganizationsIdUsersUserIdRolesPutRequest.to_json())

# convert the object into a dict
api_organizations_id_users_user_id_roles_put_request_dict = api_organizations_id_users_user_id_roles_put_request_instance.to_dict()
# create an instance of ApiOrganizationsIdUsersUserIdRolesPutRequest from a dict
api_organizations_id_users_user_id_roles_put_request_from_dict = ApiOrganizationsIdUsersUserIdRolesPutRequest.from_dict(api_organizations_id_users_user_id_roles_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


