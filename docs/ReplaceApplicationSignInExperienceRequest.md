# ReplaceApplicationSignInExperienceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branding** | [**ApiInteractionConsentGet200ResponseApplicationBranding**](ApiInteractionConsentGet200ResponseApplicationBranding.md) |  | [optional] 
**display_name** | **str** |  | [optional] 
**terms_of_use_url** | [**ReplaceApplicationSignInExperienceRequestTermsOfUseUrl**](ReplaceApplicationSignInExperienceRequestTermsOfUseUrl.md) |  | 
**privacy_policy_url** | [**ReplaceApplicationSignInExperienceRequestTermsOfUseUrl**](ReplaceApplicationSignInExperienceRequestTermsOfUseUrl.md) |  | 

## Example

```python
from py_logto.models.replace_application_sign_in_experience_request import ReplaceApplicationSignInExperienceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceApplicationSignInExperienceRequest from a JSON string
replace_application_sign_in_experience_request_instance = ReplaceApplicationSignInExperienceRequest.from_json(json)
# print the JSON string representation of the object
print(ReplaceApplicationSignInExperienceRequest.to_json())

# convert the object into a dict
replace_application_sign_in_experience_request_dict = replace_application_sign_in_experience_request_instance.to_dict()
# create an instance of ReplaceApplicationSignInExperienceRequest from a dict
replace_application_sign_in_experience_request_from_dict = ReplaceApplicationSignInExperienceRequest.from_dict(replace_application_sign_in_experience_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


