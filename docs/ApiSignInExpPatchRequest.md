# ApiSignInExpPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | [**ApiSignInExpPatchRequestColor**](ApiSignInExpPatchRequestColor.md) |  | [optional] 
**branding** | [**ApiInteractionConsentGet200ResponseApplicationBranding**](ApiInteractionConsentGet200ResponseApplicationBranding.md) |  | [optional] 
**language_info** | [**ApiSignInExpPatchRequestLanguageInfo**](ApiSignInExpPatchRequestLanguageInfo.md) |  | [optional] 
**sign_in** | [**ApiSignInExpPatchRequestSignIn**](ApiSignInExpPatchRequestSignIn.md) |  | [optional] 
**sign_up** | [**ApiSignInExpPatchRequestSignUp**](ApiSignInExpPatchRequestSignUp.md) |  | [optional] 
**social_sign_in_connector_targets** | **List[str]** | Specify the social sign-in connectors to display on the sign-in page. | [optional] 
**sign_in_mode** | **str** |  | [optional] 
**custom_css** | **str** |  | [optional] 
**custom_content** | **Dict[str, str]** | Custom content to display on experience flow pages. the page pathname will be the config key, the content will be the config value. | [optional] 
**password_policy** | [**ApiSignInExpGet200ResponsePasswordPolicy**](ApiSignInExpGet200ResponsePasswordPolicy.md) |  | [optional] 
**mfa** | [**ApiSignInExpGet200ResponseMfa**](ApiSignInExpGet200ResponseMfa.md) |  | [optional] 
**single_sign_on_enabled** | **bool** |  | [optional] 
**terms_of_use_url** | [**ApiSignInExpPatchRequestTermsOfUseUrl**](ApiSignInExpPatchRequestTermsOfUseUrl.md) |  | [optional] 
**privacy_policy_url** | [**ApiSignInExpPatchRequestTermsOfUseUrl**](ApiSignInExpPatchRequestTermsOfUseUrl.md) |  | [optional] 

## Example

```python
from py_logto.models.api_sign_in_exp_patch_request import ApiSignInExpPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSignInExpPatchRequest from a JSON string
api_sign_in_exp_patch_request_instance = ApiSignInExpPatchRequest.from_json(json)
# print the JSON string representation of the object
print(ApiSignInExpPatchRequest.to_json())

# convert the object into a dict
api_sign_in_exp_patch_request_dict = api_sign_in_exp_patch_request_instance.to_dict()
# create an instance of ApiSignInExpPatchRequest from a dict
api_sign_in_exp_patch_request_from_dict = ApiSignInExpPatchRequest.from_dict(api_sign_in_exp_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


