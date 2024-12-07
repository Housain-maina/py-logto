# CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsAuthenticatorSelection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticator_attachment** | **str** |  | [optional] 
**require_resident_key** | **bool** |  | [optional] 
**resident_key** | **str** |  | [optional] 
**user_verification** | **str** |  | [optional] 

## Example

```python
from py_logto.models.create_web_authn_registration_verification200_response_registration_options_authenticator_selection import CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsAuthenticatorSelection

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsAuthenticatorSelection from a JSON string
create_web_authn_registration_verification200_response_registration_options_authenticator_selection_instance = CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsAuthenticatorSelection.from_json(json)
# print the JSON string representation of the object
print(CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsAuthenticatorSelection.to_json())

# convert the object into a dict
create_web_authn_registration_verification200_response_registration_options_authenticator_selection_dict = create_web_authn_registration_verification200_response_registration_options_authenticator_selection_instance.to_dict()
# create an instance of CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsAuthenticatorSelection from a dict
create_web_authn_registration_verification200_response_registration_options_authenticator_selection_from_dict = CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsAuthenticatorSelection.from_dict(create_web_authn_registration_verification200_response_registration_options_authenticator_selection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


