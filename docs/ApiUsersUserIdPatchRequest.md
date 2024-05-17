# ApiUsersUserIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | [**ApiUsersUserIdPatchRequestUsername**](ApiUsersUserIdPatchRequestUsername.md) |  | [optional] 
**primary_email** | [**ApiUsersUserIdPatchRequestPrimaryEmail**](ApiUsersUserIdPatchRequestPrimaryEmail.md) |  | [optional] 
**primary_phone** | [**ApiUsersUserIdPatchRequestPrimaryPhone**](ApiUsersUserIdPatchRequestPrimaryPhone.md) |  | [optional] 
**name** | [**ApiUsersUserIdPatchRequestName**](ApiUsersUserIdPatchRequestName.md) |  | [optional] 
**avatar** | [**ApiUsersUserIdPatchRequestAvatar**](ApiUsersUserIdPatchRequestAvatar.md) |  | [optional] 
**custom_data** | **object** | Custom data object to update for the given user ID. Note this will replace the entire custom data object.  If you want to perform a partial update, use the &#x60;PATCH /api/users/{userId}/custom-data&#x60; endpoint instead. | [optional] 
**profile** | [**ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserProfile**](ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserProfile.md) |  | [optional] 

## Example

```python
from py_logto.models.api_users_user_id_patch_request import ApiUsersUserIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiUsersUserIdPatchRequest from a JSON string
api_users_user_id_patch_request_instance = ApiUsersUserIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(ApiUsersUserIdPatchRequest.to_json())

# convert the object into a dict
api_users_user_id_patch_request_dict = api_users_user_id_patch_request_instance.to_dict()
# create an instance of ApiUsersUserIdPatchRequest from a dict
api_users_user_id_patch_request_from_dict = ApiUsersUserIdPatchRequest.from_dict(api_users_user_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


