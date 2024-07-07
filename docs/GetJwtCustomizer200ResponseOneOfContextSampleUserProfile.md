# GetJwtCustomizer200ResponseOneOfContextSampleUserProfile


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
from py_logto.models.get_jwt_customizer200_response_one_of_context_sample_user_profile import GetJwtCustomizer200ResponseOneOfContextSampleUserProfile

# TODO update the JSON string below
json = "{}"
# create an instance of GetJwtCustomizer200ResponseOneOfContextSampleUserProfile from a JSON string
get_jwt_customizer200_response_one_of_context_sample_user_profile_instance = GetJwtCustomizer200ResponseOneOfContextSampleUserProfile.from_json(json)
# print the JSON string representation of the object
print(GetJwtCustomizer200ResponseOneOfContextSampleUserProfile.to_json())

# convert the object into a dict
get_jwt_customizer200_response_one_of_context_sample_user_profile_dict = get_jwt_customizer200_response_one_of_context_sample_user_profile_instance.to_dict()
# create an instance of GetJwtCustomizer200ResponseOneOfContextSampleUserProfile from a dict
get_jwt_customizer200_response_one_of_context_sample_user_profile_from_dict = GetJwtCustomizer200ResponseOneOfContextSampleUserProfile.from_dict(get_jwt_customizer200_response_one_of_context_sample_user_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


