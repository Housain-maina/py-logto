# CreateWebAuthnAuthenticationVerification200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_id** | **str** | The unique ID for the WebAuthn authentication record, required to verify the WebAuthn authentication challenge. | 
**authentication_options** | [**CreateWebAuthnAuthenticationVerification200ResponseAuthenticationOptions**](CreateWebAuthnAuthenticationVerification200ResponseAuthenticationOptions.md) |  | 

## Example

```python
from py_logto.models.create_web_authn_authentication_verification200_response import CreateWebAuthnAuthenticationVerification200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebAuthnAuthenticationVerification200Response from a JSON string
create_web_authn_authentication_verification200_response_instance = CreateWebAuthnAuthenticationVerification200Response.from_json(json)
# print the JSON string representation of the object
print(CreateWebAuthnAuthenticationVerification200Response.to_json())

# convert the object into a dict
create_web_authn_authentication_verification200_response_dict = create_web_authn_authentication_verification200_response_instance.to_dict()
# create an instance of CreateWebAuthnAuthenticationVerification200Response from a dict
create_web_authn_authentication_verification200_response_from_dict = CreateWebAuthnAuthenticationVerification200Response.from_dict(create_web_authn_authentication_verification200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


