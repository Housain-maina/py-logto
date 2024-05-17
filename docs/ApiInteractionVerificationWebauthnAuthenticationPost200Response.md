# ApiInteractionVerificationWebauthnAuthenticationPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**challenge** | **str** |  | 
**timeout** | **float** |  | [optional] 
**rp_id** | **str** |  | [optional] 
**allow_credentials** | [**List[ApiInteractionVerificationWebauthnRegistrationPost200ResponseExcludeCredentialsInner]**](ApiInteractionVerificationWebauthnRegistrationPost200ResponseExcludeCredentialsInner.md) |  | [optional] 
**user_verification** | **str** |  | [optional] 
**extensions** | [**ApiInteractionVerificationWebauthnRegistrationPost200ResponseExtensions**](ApiInteractionVerificationWebauthnRegistrationPost200ResponseExtensions.md) |  | [optional] 

## Example

```python
from py_logto.models.api_interaction_verification_webauthn_authentication_post200_response import ApiInteractionVerificationWebauthnAuthenticationPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInteractionVerificationWebauthnAuthenticationPost200Response from a JSON string
api_interaction_verification_webauthn_authentication_post200_response_instance = ApiInteractionVerificationWebauthnAuthenticationPost200Response.from_json(json)
# print the JSON string representation of the object
print(ApiInteractionVerificationWebauthnAuthenticationPost200Response.to_json())

# convert the object into a dict
api_interaction_verification_webauthn_authentication_post200_response_dict = api_interaction_verification_webauthn_authentication_post200_response_instance.to_dict()
# create an instance of ApiInteractionVerificationWebauthnAuthenticationPost200Response from a dict
api_interaction_verification_webauthn_authentication_post200_response_from_dict = ApiInteractionVerificationWebauthnAuthenticationPost200Response.from_dict(api_interaction_verification_webauthn_authentication_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


