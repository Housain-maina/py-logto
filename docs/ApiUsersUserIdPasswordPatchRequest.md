# ApiUsersUserIdPasswordPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | New password for the user. | 

## Example

```python
from py_logto.models.api_users_user_id_password_patch_request import ApiUsersUserIdPasswordPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiUsersUserIdPasswordPatchRequest from a JSON string
api_users_user_id_password_patch_request_instance = ApiUsersUserIdPasswordPatchRequest.from_json(json)
# print the JSON string representation of the object
print(ApiUsersUserIdPasswordPatchRequest.to_json())

# convert the object into a dict
api_users_user_id_password_patch_request_dict = api_users_user_id_password_patch_request_instance.to_dict()
# create an instance of ApiUsersUserIdPasswordPatchRequest from a dict
api_users_user_id_password_patch_request_from_dict = ApiUsersUserIdPasswordPatchRequest.from_dict(api_users_user_id_password_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


