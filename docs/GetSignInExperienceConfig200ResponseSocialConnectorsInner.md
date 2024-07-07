# GetSignInExperienceConfig200ResponseSocialConnectorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**target** | **str** |  | 
**name** | **object** | Validator function | 
**logo** | **str** |  | 
**logo_dark** | **str** |  | 
**from_email** | **str** |  | [optional] 
**platform** | **str** |  | 
**is_standard** | **bool** |  | [optional] 

## Example

```python
from py_logto.models.get_sign_in_experience_config200_response_social_connectors_inner import GetSignInExperienceConfig200ResponseSocialConnectorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSignInExperienceConfig200ResponseSocialConnectorsInner from a JSON string
get_sign_in_experience_config200_response_social_connectors_inner_instance = GetSignInExperienceConfig200ResponseSocialConnectorsInner.from_json(json)
# print the JSON string representation of the object
print(GetSignInExperienceConfig200ResponseSocialConnectorsInner.to_json())

# convert the object into a dict
get_sign_in_experience_config200_response_social_connectors_inner_dict = get_sign_in_experience_config200_response_social_connectors_inner_instance.to_dict()
# create an instance of GetSignInExperienceConfig200ResponseSocialConnectorsInner from a dict
get_sign_in_experience_config200_response_social_connectors_inner_from_dict = GetSignInExperienceConfig200ResponseSocialConnectorsInner.from_dict(get_sign_in_experience_config200_response_social_connectors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


