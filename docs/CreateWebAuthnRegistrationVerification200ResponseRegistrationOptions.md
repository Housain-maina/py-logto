# CreateWebAuthnRegistrationVerification200ResponseRegistrationOptions

The WebAuthn registration options that the user needs to create a new WebAuthn credential.

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
from py_logto.models.create_web_authn_registration_verification200_response_registration_options import CreateWebAuthnRegistrationVerification200ResponseRegistrationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebAuthnRegistrationVerification200ResponseRegistrationOptions from a JSON string
create_web_authn_registration_verification200_response_registration_options_instance = CreateWebAuthnRegistrationVerification200ResponseRegistrationOptions.from_json(json)
# print the JSON string representation of the object
print(CreateWebAuthnRegistrationVerification200ResponseRegistrationOptions.to_json())

# convert the object into a dict
create_web_authn_registration_verification200_response_registration_options_dict = create_web_authn_registration_verification200_response_registration_options_instance.to_dict()
# create an instance of CreateWebAuthnRegistrationVerification200ResponseRegistrationOptions from a dict
create_web_authn_registration_verification200_response_registration_options_from_dict = CreateWebAuthnRegistrationVerification200ResponseRegistrationOptions.from_dict(create_web_authn_registration_verification200_response_registration_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


