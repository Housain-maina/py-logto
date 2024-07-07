# GetSignInExperienceConfig200ResponseGoogleOneTap


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** |  | [optional] 
**auto_select** | **bool** |  | [optional] 
**close_on_tap_outside** | **bool** |  | [optional] 
**itp_support** | **bool** |  | [optional] 
**client_id** | **str** |  | 
**connector_id** | **str** |  | 

## Example

```python
from py_logto.models.get_sign_in_experience_config200_response_google_one_tap import GetSignInExperienceConfig200ResponseGoogleOneTap

# TODO update the JSON string below
json = "{}"
# create an instance of GetSignInExperienceConfig200ResponseGoogleOneTap from a JSON string
get_sign_in_experience_config200_response_google_one_tap_instance = GetSignInExperienceConfig200ResponseGoogleOneTap.from_json(json)
# print the JSON string representation of the object
print(GetSignInExperienceConfig200ResponseGoogleOneTap.to_json())

# convert the object into a dict
get_sign_in_experience_config200_response_google_one_tap_dict = get_sign_in_experience_config200_response_google_one_tap_instance.to_dict()
# create an instance of GetSignInExperienceConfig200ResponseGoogleOneTap from a dict
get_sign_in_experience_config200_response_google_one_tap_from_dict = GetSignInExperienceConfig200ResponseGoogleOneTap.from_dict(get_sign_in_experience_config200_response_google_one_tap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


