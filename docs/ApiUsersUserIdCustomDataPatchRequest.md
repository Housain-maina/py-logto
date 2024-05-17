# ApiUsersUserIdCustomDataPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_data** | **object** | Partial custom data object to update for the given user ID. | 

## Example

```python
from py_logto.models.api_users_user_id_custom_data_patch_request import ApiUsersUserIdCustomDataPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiUsersUserIdCustomDataPatchRequest from a JSON string
api_users_user_id_custom_data_patch_request_instance = ApiUsersUserIdCustomDataPatchRequest.from_json(json)
# print the JSON string representation of the object
print(ApiUsersUserIdCustomDataPatchRequest.to_json())

# convert the object into a dict
api_users_user_id_custom_data_patch_request_dict = api_users_user_id_custom_data_patch_request_instance.to_dict()
# create an instance of ApiUsersUserIdCustomDataPatchRequest from a dict
api_users_user_id_custom_data_patch_request_from_dict = ApiUsersUserIdCustomDataPatchRequest.from_dict(api_users_user_id_custom_data_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


