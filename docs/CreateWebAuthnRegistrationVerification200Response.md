# CreateWebAuthnRegistrationVerification200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_id** | **str** | The unique verification ID for the WebAuthn registration record. This ID is required to verify the WebAuthn registration challenge. | 
**registration_options** | [**CreateWebAuthnRegistrationVerification200ResponseRegistrationOptions**](CreateWebAuthnRegistrationVerification200ResponseRegistrationOptions.md) |  | 

## Example

```python
from py_logto.models.create_web_authn_registration_verification200_response import CreateWebAuthnRegistrationVerification200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebAuthnRegistrationVerification200Response from a JSON string
create_web_authn_registration_verification200_response_instance = CreateWebAuthnRegistrationVerification200Response.from_json(json)
# print the JSON string representation of the object
print(CreateWebAuthnRegistrationVerification200Response.to_json())

# convert the object into a dict
create_web_authn_registration_verification200_response_dict = create_web_authn_registration_verification200_response_instance.to_dict()
# create an instance of CreateWebAuthnRegistrationVerification200Response from a dict
create_web_authn_registration_verification200_response_from_dict = CreateWebAuthnRegistrationVerification200Response.from_dict(create_web_authn_registration_verification200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


