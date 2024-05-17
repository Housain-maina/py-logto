# ApiSignInExpGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**color** | [**ApiSignInExpGet200ResponseColor**](ApiSignInExpGet200ResponseColor.md) |  | 
**branding** | [**ApiInteractionConsentGet200ResponseApplicationBranding**](ApiInteractionConsentGet200ResponseApplicationBranding.md) |  | 
**language_info** | [**ApiSignInExpGet200ResponseLanguageInfo**](ApiSignInExpGet200ResponseLanguageInfo.md) |  | 
**terms_of_use_url** | **str** |  | 
**privacy_policy_url** | **str** |  | 
**sign_in** | [**ApiSignInExpGet200ResponseSignIn**](ApiSignInExpGet200ResponseSignIn.md) |  | 
**sign_up** | [**ApiSignInExpGet200ResponseSignUp**](ApiSignInExpGet200ResponseSignUp.md) |  | 
**social_sign_in_connector_targets** | **List[str]** | Enabled social sign-in connectors, will displayed on the sign-in page. | 
**sign_in_mode** | **str** |  | 
**custom_css** | **str** |  | 
**custom_content** | **Dict[str, str]** | Custom content to display on experience flow pages. the page pathname will be the config key, the content will be the config value. | 
**password_policy** | [**ApiSignInExpGet200ResponsePasswordPolicy**](ApiSignInExpGet200ResponsePasswordPolicy.md) |  | 
**mfa** | [**ApiSignInExpGet200ResponseMfa**](ApiSignInExpGet200ResponseMfa.md) |  | 
**single_sign_on_enabled** | **bool** |  | 

## Example

```python
from py_logto.models.api_sign_in_exp_get200_response import ApiSignInExpGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSignInExpGet200Response from a JSON string
api_sign_in_exp_get200_response_instance = ApiSignInExpGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiSignInExpGet200Response.to_json())

# convert the object into a dict
api_sign_in_exp_get200_response_dict = api_sign_in_exp_get200_response_instance.to_dict()
# create an instance of ApiSignInExpGet200Response from a dict
api_sign_in_exp_get200_response_from_dict = ApiSignInExpGet200Response.from_dict(api_sign_in_exp_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


