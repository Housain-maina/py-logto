# VerifyWebAuthnRegistrationVerificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_id** | **str** | The verification ID of the WebAuthn registration record. | 
**payload** | [**VerifyWebAuthnRegistrationVerificationRequestPayload**](VerifyWebAuthnRegistrationVerificationRequestPayload.md) |  | 

## Example

```python
from py_logto.models.verify_web_authn_registration_verification_request import VerifyWebAuthnRegistrationVerificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyWebAuthnRegistrationVerificationRequest from a JSON string
verify_web_authn_registration_verification_request_instance = VerifyWebAuthnRegistrationVerificationRequest.from_json(json)
# print the JSON string representation of the object
print(VerifyWebAuthnRegistrationVerificationRequest.to_json())

# convert the object into a dict
verify_web_authn_registration_verification_request_dict = verify_web_authn_registration_verification_request_instance.to_dict()
# create an instance of VerifyWebAuthnRegistrationVerificationRequest from a dict
verify_web_authn_registration_verification_request_from_dict = VerifyWebAuthnRegistrationVerificationRequest.from_dict(verify_web_authn_registration_verification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


