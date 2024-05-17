# ApiUsersUserIdIsSuspendedPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_suspended** | **bool** | New suspension status for the user. | 

## Example

```python
from py_logto.models.api_users_user_id_is_suspended_patch_request import ApiUsersUserIdIsSuspendedPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiUsersUserIdIsSuspendedPatchRequest from a JSON string
api_users_user_id_is_suspended_patch_request_instance = ApiUsersUserIdIsSuspendedPatchRequest.from_json(json)
# print the JSON string representation of the object
print(ApiUsersUserIdIsSuspendedPatchRequest.to_json())

# convert the object into a dict
api_users_user_id_is_suspended_patch_request_dict = api_users_user_id_is_suspended_patch_request_instance.to_dict()
# create an instance of ApiUsersUserIdIsSuspendedPatchRequest from a dict
api_users_user_id_is_suspended_patch_request_from_dict = ApiUsersUserIdIsSuspendedPatchRequest.from_dict(api_users_user_id_is_suspended_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


