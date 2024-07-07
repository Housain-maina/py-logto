# UpdateSignInExp200Response


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

## Example

```python
from py_logto.models.update_sign_in_exp200_response import UpdateSignInExp200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSignInExp200Response from a JSON string
update_sign_in_exp200_response_instance = UpdateSignInExp200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateSignInExp200Response.to_json())

# convert the object into a dict
update_sign_in_exp200_response_dict = update_sign_in_exp200_response_instance.to_dict()
# create an instance of UpdateSignInExp200Response from a dict
update_sign_in_exp200_response_from_dict = UpdateSignInExp200Response.from_dict(update_sign_in_exp200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


