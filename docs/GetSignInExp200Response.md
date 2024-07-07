# GetSignInExp200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**id** | **str** |  | 
**color** | [**GetSignInExp200ResponseColor**](GetSignInExp200ResponseColor.md) |  | 
**branding** | [**ApiInteractionConsentGet200ResponseApplicationBranding**](ApiInteractionConsentGet200ResponseApplicationBranding.md) |  | 
**language_info** | [**GetSignInExp200ResponseLanguageInfo**](GetSignInExp200ResponseLanguageInfo.md) |  | 
**terms_of_use_url** | **str** |  | 
**privacy_policy_url** | **str** |  | 
**agree_to_terms_policy** | **str** |  | 
**sign_in** | [**GetSignInExp200ResponseSignIn**](GetSignInExp200ResponseSignIn.md) |  | 
**sign_up** | [**GetSignInExp200ResponseSignUp**](GetSignInExp200ResponseSignUp.md) |  | 
**social_sign_in** | [**GetSignInExp200ResponseSocialSignIn**](GetSignInExp200ResponseSocialSignIn.md) |  | 
**social_sign_in_connector_targets** | **List[str]** | Enabled social sign-in connectors, will displayed on the sign-in page. | 
**sign_in_mode** | **str** |  | 
**custom_css** | **str** |  | 
**custom_content** | **Dict[str, str]** | Custom content to display on experience flow pages. the page pathname will be the config key, the content will be the config value. | 
**custom_ui_asset_id** | **str** |  | 
**password_policy** | [**GetSignInExp200ResponsePasswordPolicy**](GetSignInExp200ResponsePasswordPolicy.md) |  | 
**mfa** | [**GetSignInExp200ResponseMfa**](GetSignInExp200ResponseMfa.md) |  | 
**single_sign_on_enabled** | **bool** |  | 

## Example

```python
from py_logto.models.get_sign_in_exp200_response import GetSignInExp200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSignInExp200Response from a JSON string
get_sign_in_exp200_response_instance = GetSignInExp200Response.from_json(json)
# print the JSON string representation of the object
print(GetSignInExp200Response.to_json())

# convert the object into a dict
get_sign_in_exp200_response_dict = get_sign_in_exp200_response_instance.to_dict()
# create an instance of GetSignInExp200Response from a dict
get_sign_in_exp200_response_from_dict = GetSignInExp200Response.from_dict(get_sign_in_exp200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


