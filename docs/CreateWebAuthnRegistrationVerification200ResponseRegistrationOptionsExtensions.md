# CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsExtensions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appid** | **str** |  | [optional] 
**cred_props** | **bool** |  | [optional] 
**hmac_create_secret** | **bool** |  | [optional] 

## Example

```python
from py_logto.models.create_web_authn_registration_verification200_response_registration_options_extensions import CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsExtensions

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsExtensions from a JSON string
create_web_authn_registration_verification200_response_registration_options_extensions_instance = CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsExtensions.from_json(json)
# print the JSON string representation of the object
print(CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsExtensions.to_json())

# convert the object into a dict
create_web_authn_registration_verification200_response_registration_options_extensions_dict = create_web_authn_registration_verification200_response_registration_options_extensions_instance.to_dict()
# create an instance of CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsExtensions from a dict
create_web_authn_registration_verification200_response_registration_options_extensions_from_dict = CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsExtensions.from_dict(create_web_authn_registration_verification200_response_registration_options_extensions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


