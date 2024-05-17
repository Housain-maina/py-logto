# ApiInteractionVerificationWebauthnRegistrationPost200ResponseAuthenticatorSelection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticator_attachment** | **str** |  | [optional] 
**require_resident_key** | **bool** |  | [optional] 
**resident_key** | **str** |  | [optional] 
**user_verification** | **str** |  | [optional] 

## Example

```python
from py_logto.models.api_interaction_verification_webauthn_registration_post200_response_authenticator_selection import ApiInteractionVerificationWebauthnRegistrationPost200ResponseAuthenticatorSelection

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInteractionVerificationWebauthnRegistrationPost200ResponseAuthenticatorSelection from a JSON string
api_interaction_verification_webauthn_registration_post200_response_authenticator_selection_instance = ApiInteractionVerificationWebauthnRegistrationPost200ResponseAuthenticatorSelection.from_json(json)
# print the JSON string representation of the object
print(ApiInteractionVerificationWebauthnRegistrationPost200ResponseAuthenticatorSelection.to_json())

# convert the object into a dict
api_interaction_verification_webauthn_registration_post200_response_authenticator_selection_dict = api_interaction_verification_webauthn_registration_post200_response_authenticator_selection_instance.to_dict()
# create an instance of ApiInteractionVerificationWebauthnRegistrationPost200ResponseAuthenticatorSelection from a dict
api_interaction_verification_webauthn_registration_post200_response_authenticator_selection_from_dict = ApiInteractionVerificationWebauthnRegistrationPost200ResponseAuthenticatorSelection.from_dict(api_interaction_verification_webauthn_registration_post200_response_authenticator_selection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


