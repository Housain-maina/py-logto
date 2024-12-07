# GetSignInExp200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**id** | **str** |  | 
**color** | [**GetSignInExp200ResponseColor**](GetSignInExp200ResponseColor.md) |  | 
**branding** | [**ListApplicationOrganizations200ResponseInnerBranding**](ListApplicationOrganizations200ResponseInnerBranding.md) |  | 
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
**custom_ui_assets** | [**GetSignInExp200ResponseCustomUiAssets**](GetSignInExp200ResponseCustomUiAssets.md) |  | 
**password_policy** | [**GetSignInExp200ResponsePasswordPolicy**](GetSignInExp200ResponsePasswordPolicy.md) |  | 
**mfa** | [**GetSignInExp200ResponseMfa**](GetSignInExp200ResponseMfa.md) |  | 
**single_sign_on_enabled** | **bool** |  | 
**support_email** | **str** | The support email address to display on the error pages. | 
**support_website_url** | **str** | The support website URL to display on the error pages. | 
**unknown_session_redirect_url** | **str** | The fallback URL to redirect users when the sign-in session does not exist or unknown. Client should initiates a new authentication flow after the redirection. | 

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


