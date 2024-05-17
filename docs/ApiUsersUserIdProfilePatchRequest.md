# ApiUsersUserIdProfilePatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**ApiUsersUserIdProfilePatchRequestProfile**](ApiUsersUserIdProfilePatchRequestProfile.md) |  | 

## Example

```python
from py_logto.models.api_users_user_id_profile_patch_request import ApiUsersUserIdProfilePatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiUsersUserIdProfilePatchRequest from a JSON string
api_users_user_id_profile_patch_request_instance = ApiUsersUserIdProfilePatchRequest.from_json(json)
# print the JSON string representation of the object
print(ApiUsersUserIdProfilePatchRequest.to_json())

# convert the object into a dict
api_users_user_id_profile_patch_request_dict = api_users_user_id_profile_patch_request_instance.to_dict()
# create an instance of ApiUsersUserIdProfilePatchRequest from a dict
api_users_user_id_profile_patch_request_from_dict = ApiUsersUserIdProfilePatchRequest.from_dict(api_users_user_id_profile_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


