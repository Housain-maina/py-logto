# VerifyWebAuthnAuthenticationVerificationRequestPayload

The WebAuthn assertion response from the user's WebAuthn credential.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | 
**raw_id** | **str** |  | 
**authenticator_attachment** | **str** |  | [optional] 
**client_extension_results** | [**VerifyWebAuthnRegistrationVerificationRequestPayloadClientExtensionResults**](VerifyWebAuthnRegistrationVerificationRequestPayloadClientExtensionResults.md) |  | 
**response** | [**VerifyWebAuthnAuthenticationVerificationRequestPayloadResponse**](VerifyWebAuthnAuthenticationVerificationRequestPayloadResponse.md) |  | 

## Example

```python
from py_logto.models.verify_web_authn_authentication_verification_request_payload import VerifyWebAuthnAuthenticationVerificationRequestPayload

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyWebAuthnAuthenticationVerificationRequestPayload from a JSON string
verify_web_authn_authentication_verification_request_payload_instance = VerifyWebAuthnAuthenticationVerificationRequestPayload.from_json(json)
# print the JSON string representation of the object
print(VerifyWebAuthnAuthenticationVerificationRequestPayload.to_json())

# convert the object into a dict
verify_web_authn_authentication_verification_request_payload_dict = verify_web_authn_authentication_verification_request_payload_instance.to_dict()
# create an instance of VerifyWebAuthnAuthenticationVerificationRequestPayload from a dict
verify_web_authn_authentication_verification_request_payload_from_dict = VerifyWebAuthnAuthenticationVerificationRequestPayload.from_dict(verify_web_authn_authentication_verification_request_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


