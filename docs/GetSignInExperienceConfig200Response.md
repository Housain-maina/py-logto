# GetSignInExperienceConfig200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**id** | **str** |  | 
**color** | [**UpdateSignInExp200ResponseColor**](UpdateSignInExp200ResponseColor.md) |  | 
**branding** | [**ApiInteractionConsentGet200ResponseApplicationBranding**](ApiInteractionConsentGet200ResponseApplicationBranding.md) |  | 
**language_info** | [**UpdateSignInExp200ResponseLanguageInfo**](UpdateSignInExp200ResponseLanguageInfo.md) |  | 
**terms_of_use_url** | **str** |  | 
**privacy_policy_url** | **str** |  | 
**agree_to_terms_policy** | **str** |  | 
**sign_in** | [**UpdateSignInExp200ResponseSignIn**](UpdateSignInExp200ResponseSignIn.md) |  | 
**sign_up** | [**UpdateSignInExp200ResponseSignUp**](UpdateSignInExp200ResponseSignUp.md) |  | 
**social_sign_in** | [**GetSignInExp200ResponseSocialSignIn**](GetSignInExp200ResponseSocialSignIn.md) |  | 
**social_sign_in_connector_targets** | **List[str]** |  | 
**sign_in_mode** | **str** |  | 
**custom_css** | **str** |  | 
**custom_content** | **Dict[str, str]** |  | 
**custom_ui_asset_id** | **str** |  | 
**password_policy** | [**UpdateSignInExp200ResponsePasswordPolicy**](UpdateSignInExp200ResponsePasswordPolicy.md) |  | 
**mfa** | [**UpdateSignInExp200ResponseMfa**](UpdateSignInExp200ResponseMfa.md) |  | 
**single_sign_on_enabled** | **bool** |  | 
**social_connectors** | [**List[GetSignInExperienceConfig200ResponseSocialConnectorsInner]**](GetSignInExperienceConfig200ResponseSocialConnectorsInner.md) |  | 
**sso_connectors** | [**List[GetSignInExperienceConfig200ResponseSsoConnectorsInner]**](GetSignInExperienceConfig200ResponseSsoConnectorsInner.md) |  | 
**forgot_password** | [**GetSignInExperienceConfig200ResponseForgotPassword**](GetSignInExperienceConfig200ResponseForgotPassword.md) |  | 
**is_development_tenant** | **bool** |  | 
**google_one_tap** | [**GetSignInExperienceConfig200ResponseGoogleOneTap**](GetSignInExperienceConfig200ResponseGoogleOneTap.md) |  | [optional] 

## Example

```python
from py_logto.models.get_sign_in_experience_config200_response import GetSignInExperienceConfig200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSignInExperienceConfig200Response from a JSON string
get_sign_in_experience_config200_response_instance = GetSignInExperienceConfig200Response.from_json(json)
# print the JSON string representation of the object
print(GetSignInExperienceConfig200Response.to_json())

# convert the object into a dict
get_sign_in_experience_config200_response_dict = get_sign_in_experience_config200_response_instance.to_dict()
# create an instance of GetSignInExperienceConfig200Response from a dict
get_sign_in_experience_config200_response_from_dict = GetSignInExperienceConfig200Response.from_dict(get_sign_in_experience_config200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


