# UpdateUserProfileRequestProfile

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
**address** | [**GetJwtCustomizer200ResponseOneOfContextSampleUserProfileAddress**](GetJwtCustomizer200ResponseOneOfContextSampleUserProfileAddress.md) |  | [optional] 

## Example

```python
from py_logto.models.update_user_profile_request_profile import UpdateUserProfileRequestProfile

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserProfileRequestProfile from a JSON string
update_user_profile_request_profile_instance = UpdateUserProfileRequestProfile.from_json(json)
# print the JSON string representation of the object
print(UpdateUserProfileRequestProfile.to_json())

# convert the object into a dict
update_user_profile_request_profile_dict = update_user_profile_request_profile_instance.to_dict()
# create an instance of UpdateUserProfileRequestProfile from a dict
update_user_profile_request_profile_from_dict = UpdateUserProfileRequestProfile.from_dict(update_user_profile_request_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


