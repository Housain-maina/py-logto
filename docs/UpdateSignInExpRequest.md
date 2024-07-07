# UpdateSignInExpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 
**color** | [**UpdateSignInExpRequestColor**](UpdateSignInExpRequestColor.md) |  | [optional] 
**branding** | [**ApiInteractionConsentGet200ResponseApplicationBranding**](ApiInteractionConsentGet200ResponseApplicationBranding.md) |  | [optional] 
**language_info** | [**UpdateSignInExpRequestLanguageInfo**](UpdateSignInExpRequestLanguageInfo.md) |  | [optional] 
**agree_to_terms_policy** | **str** |  | [optional] 
**sign_in** | [**UpdateSignInExpRequestSignIn**](UpdateSignInExpRequestSignIn.md) |  | [optional] 
**sign_up** | [**UpdateSignInExpRequestSignUp**](UpdateSignInExpRequestSignUp.md) |  | [optional] 
**social_sign_in** | [**GetSignInExp200ResponseSocialSignIn**](GetSignInExp200ResponseSocialSignIn.md) |  | [optional] 
**social_sign_in_connector_targets** | **List[str]** | Specify the social sign-in connectors to display on the sign-in page. | [optional] 
**sign_in_mode** | **str** |  | [optional] 
**custom_css** | **str** |  | [optional] 
**custom_content** | **Dict[str, str]** | Custom content to display on experience flow pages. the page pathname will be the config key, the content will be the config value. | [optional] 
**custom_ui_asset_id** | **str** |  | [optional] 
**password_policy** | [**GetSignInExp200ResponsePasswordPolicy**](GetSignInExp200ResponsePasswordPolicy.md) |  | [optional] 
**mfa** | [**GetSignInExp200ResponseMfa**](GetSignInExp200ResponseMfa.md) |  | [optional] 
**single_sign_on_enabled** | **bool** |  | [optional] 
**terms_of_use_url** | [**UpdateSignInExpRequestTermsOfUseUrl**](UpdateSignInExpRequestTermsOfUseUrl.md) |  | [optional] 
**privacy_policy_url** | [**UpdateSignInExpRequestTermsOfUseUrl**](UpdateSignInExpRequestTermsOfUseUrl.md) |  | [optional] 

## Example

```python
from py_logto.models.update_sign_in_exp_request import UpdateSignInExpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSignInExpRequest from a JSON string
update_sign_in_exp_request_instance = UpdateSignInExpRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSignInExpRequest.to_json())

# convert the object into a dict
update_sign_in_exp_request_dict = update_sign_in_exp_request_instance.to_dict()
# create an instance of UpdateSignInExpRequest from a dict
update_sign_in_exp_request_from_dict = UpdateSignInExpRequest.from_dict(update_sign_in_exp_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


