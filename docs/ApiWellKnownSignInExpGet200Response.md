# ApiWellKnownSignInExpGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**color** | [**ApiSignInExpPatch200ResponseColor**](ApiSignInExpPatch200ResponseColor.md) |  | 
**branding** | [**ApiInteractionConsentGet200ResponseApplicationBranding**](ApiInteractionConsentGet200ResponseApplicationBranding.md) |  | 
**language_info** | [**ApiSignInExpPatch200ResponseLanguageInfo**](ApiSignInExpPatch200ResponseLanguageInfo.md) |  | 
**terms_of_use_url** | **str** |  | 
**privacy_policy_url** | **str** |  | 
**sign_in** | [**ApiSignInExpPatch200ResponseSignIn**](ApiSignInExpPatch200ResponseSignIn.md) |  | 
**sign_up** | [**ApiSignInExpPatch200ResponseSignUp**](ApiSignInExpPatch200ResponseSignUp.md) |  | 
**social_sign_in_connector_targets** | **List[str]** |  | 
**sign_in_mode** | **str** |  | 
**custom_css** | **str** |  | 
**custom_content** | **Dict[str, str]** |  | 
**password_policy** | [**ApiSignInExpPatch200ResponsePasswordPolicy**](ApiSignInExpPatch200ResponsePasswordPolicy.md) |  | 
**mfa** | [**ApiSignInExpPatch200ResponseMfa**](ApiSignInExpPatch200ResponseMfa.md) |  | 
**single_sign_on_enabled** | **bool** |  | 
**social_connectors** | [**List[ApiWellKnownSignInExpGet200ResponseSocialConnectorsInner]**](ApiWellKnownSignInExpGet200ResponseSocialConnectorsInner.md) |  | 
**sso_connectors** | [**List[ApiWellKnownSignInExpGet200ResponseSsoConnectorsInner]**](ApiWellKnownSignInExpGet200ResponseSsoConnectorsInner.md) |  | 
**forgot_password** | [**ApiWellKnownSignInExpGet200ResponseForgotPassword**](ApiWellKnownSignInExpGet200ResponseForgotPassword.md) |  | 
**is_development_tenant** | **bool** |  | 

## Example

```python
from py_logto.models.api_well_known_sign_in_exp_get200_response import ApiWellKnownSignInExpGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiWellKnownSignInExpGet200Response from a JSON string
api_well_known_sign_in_exp_get200_response_instance = ApiWellKnownSignInExpGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiWellKnownSignInExpGet200Response.to_json())

# convert the object into a dict
api_well_known_sign_in_exp_get200_response_dict = api_well_known_sign_in_exp_get200_response_instance.to_dict()
# create an instance of ApiWellKnownSignInExpGet200Response from a dict
api_well_known_sign_in_exp_get200_response_from_dict = ApiWellKnownSignInExpGet200Response.from_dict(api_well_known_sign_in_exp_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


