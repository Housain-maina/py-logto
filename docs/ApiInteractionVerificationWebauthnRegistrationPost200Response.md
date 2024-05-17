# ApiInteractionVerificationWebauthnRegistrationPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rp** | [**ApiInteractionVerificationWebauthnRegistrationPost200ResponseRp**](ApiInteractionVerificationWebauthnRegistrationPost200ResponseRp.md) |  | 
**user** | [**ApiInteractionVerificationWebauthnRegistrationPost200ResponseUser**](ApiInteractionVerificationWebauthnRegistrationPost200ResponseUser.md) |  | 
**challenge** | **str** |  | 
**pub_key_cred_params** | [**List[ApiInteractionVerificationWebauthnRegistrationPost200ResponsePubKeyCredParamsInner]**](ApiInteractionVerificationWebauthnRegistrationPost200ResponsePubKeyCredParamsInner.md) |  | 
**timeout** | **float** |  | [optional] 
**exclude_credentials** | [**List[ApiInteractionVerificationWebauthnRegistrationPost200ResponseExcludeCredentialsInner]**](ApiInteractionVerificationWebauthnRegistrationPost200ResponseExcludeCredentialsInner.md) |  | [optional] 
**authenticator_selection** | [**ApiInteractionVerificationWebauthnRegistrationPost200ResponseAuthenticatorSelection**](ApiInteractionVerificationWebauthnRegistrationPost200ResponseAuthenticatorSelection.md) |  | [optional] 
**attestation** | **str** |  | [optional] 
**extensions** | [**ApiInteractionVerificationWebauthnRegistrationPost200ResponseExtensions**](ApiInteractionVerificationWebauthnRegistrationPost200ResponseExtensions.md) |  | [optional] 

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


