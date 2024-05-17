# ApiUsersUserIdProfilePatchRequestProfile

Partial profile object to update for the given user ID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**family_name** | **str** |  | [optional] 
**given_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**nickname** | **str** |  | [optional] 
**preferred_username** | **str** |  | [optional] 
**profile** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**birthdate** | **str** |  | [optional] 
**zoneinfo** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**address** | [**ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserProfileAddress**](ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserProfileAddress.md) |  | [optional] 

## Example

```python
from py_logto.models.api_users_user_id_profile_patch_request_profile import ApiUsersUserIdProfilePatchRequestProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ApiUsersUserIdProfilePatchRequestProfile from a JSON string
api_users_user_id_profile_patch_request_profile_instance = ApiUsersUserIdProfilePatchRequestProfile.from_json(json)
# print the JSON string representation of the object
print(ApiUsersUserIdProfilePatchRequestProfile.to_json())

# convert the object into a dict
api_users_user_id_profile_patch_request_profile_dict = api_users_user_id_profile_patch_request_profile_instance.to_dict()
# create an instance of ApiUsersUserIdProfilePatchRequestProfile from a dict
api_users_user_id_profile_patch_request_profile_from_dict = ApiUsersUserIdProfilePatchRequestProfile.from_dict(api_users_user_id_profile_patch_request_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


