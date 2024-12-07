# VerifyWebAuthnRegistrationVerificationRequestPayloadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_data_json** | **str** |  | 
**attestation_object** | **str** |  | 
**authenticator_data** | **str** |  | [optional] 
**transports** | **List[str]** |  | [optional] 
**public_key_algorithm** | **float** |  | [optional] 
**public_key** | **str** |  | [optional] 

## Example

```python
from py_logto.models.verify_web_authn_registration_verification_request_payload_response import VerifyWebAuthnRegistrationVerificationRequestPayloadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyWebAuthnRegistrationVerificationRequestPayloadResponse from a JSON string
verify_web_authn_registration_verification_request_payload_response_instance = VerifyWebAuthnRegistrationVerificationRequestPayloadResponse.from_json(json)
# print the JSON string representation of the object
print(VerifyWebAuthnRegistrationVerificationRequestPayloadResponse.to_json())

# convert the object into a dict
verify_web_authn_registration_verification_request_payload_response_dict = verify_web_authn_registration_verification_request_payload_response_instance.to_dict()
# create an instance of VerifyWebAuthnRegistrationVerificationRequestPayloadResponse from a dict
verify_web_authn_registration_verification_request_payload_response_from_dict = VerifyWebAuthnRegistrationVerificationRequestPayloadResponse.from_dict(verify_web_authn_registration_verification_request_payload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


