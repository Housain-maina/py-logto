# ApiInteractionVerificationWebauthnRegistrationPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rp** | [**CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsRp**](CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsRp.md) |  | 
**user** | [**CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsUser**](CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsUser.md) |  | 
**challenge** | **str** |  | 
**pub_key_cred_params** | [**List[CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsPubKeyCredParamsInner]**](CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsPubKeyCredParamsInner.md) |  | 
**timeout** | **float** |  | [optional] 
**exclude_credentials** | [**List[CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsExcludeCredentialsInner]**](CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsExcludeCredentialsInner.md) |  | [optional] 
**authenticator_selection** | [**CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsAuthenticatorSelection**](CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsAuthenticatorSelection.md) |  | [optional] 
**attestation** | **str** |  | [optional] 
**extensions** | [**CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsExtensions**](CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsExtensions.md) |  | [optional] 

## Example

```python
from py_logto.models.api_interaction_verification_webauthn_registration_post200_response import ApiInteractionVerificationWebauthnRegistrationPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInteractionVerificationWebauthnRegistrationPost200Response from a JSON string
api_interaction_verification_webauthn_registration_post200_response_instance = ApiInteractionVerificationWebauthnRegistrationPost200Response.from_json(json)
# print the JSON string representation of the object
print(ApiInteractionVerificationWebauthnRegistrationPost200Response.to_json())

# convert the object into a dict
api_interaction_verification_webauthn_registration_post200_response_dict = api_interaction_verification_webauthn_registration_post200_response_instance.to_dict()
# create an instance of ApiInteractionVerificationWebauthnRegistrationPost200Response from a dict
api_interaction_verification_webauthn_registration_post200_response_from_dict = ApiInteractionVerificationWebauthnRegistrationPost200Response.from_dict(api_interaction_verification_webauthn_registration_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


