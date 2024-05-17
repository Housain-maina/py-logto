# ApiRolesIdUsersPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[str]** | An array of user IDs to be assigned. | 

## Example

```python
from py_logto.models.api_roles_id_users_post_request import ApiRolesIdUsersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiRolesIdUsersPostRequest from a JSON string
api_roles_id_users_post_request_instance = ApiRolesIdUsersPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiRolesIdUsersPostRequest.to_json())

# convert the object into a dict
api_roles_id_users_post_request_dict = api_roles_id_users_post_request_instance.to_dict()
# create an instance of ApiRolesIdUsersPostRequest from a dict
api_roles_id_users_post_request_from_dict = ApiRolesIdUsersPostRequest.from_dict(api_roles_id_users_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


