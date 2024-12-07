# VerifyWebAuthnRegistrationVerificationRequestPayload

The WebAuthn attestation response from the user's WebAuthn credential.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | 
**raw_id** | **str** |  | 
**response** | [**VerifyWebAuthnRegistrationVerificationRequestPayloadResponse**](VerifyWebAuthnRegistrationVerificationRequestPayloadResponse.md) |  | 
**authenticator_attachment** | **str** |  | [optional] 
**client_extension_results** | [**VerifyWebAuthnRegistrationVerificationRequestPayloadClientExtensionResults**](VerifyWebAuthnRegistrationVerificationRequestPayloadClientExtensionResults.md) |  | 

## Example

```python
from py_logto.models.verify_web_authn_registration_verification_request_payload import VerifyWebAuthnRegistrationVerificationRequestPayload

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyWebAuthnRegistrationVerificationRequestPayload from a JSON string
verify_web_authn_registration_verification_request_payload_instance = VerifyWebAuthnRegistrationVerificationRequestPayload.from_json(json)
# print the JSON string representation of the object
print(VerifyWebAuthnRegistrationVerificationRequestPayload.to_json())

# convert the object into a dict
verify_web_authn_registration_verification_request_payload_dict = verify_web_authn_registration_verification_request_payload_instance.to_dict()
# create an instance of VerifyWebAuthnRegistrationVerificationRequestPayload from a dict
verify_web_authn_registration_verification_request_payload_from_dict = VerifyWebAuthnRegistrationVerificationRequestPayload.from_dict(verify_web_authn_registration_verification_request_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


