# VerifyWebAuthnAuthenticationVerificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_id** | **str** | The verification ID of the WebAuthn authentication verification record. | 
**payload** | [**VerifyWebAuthnAuthenticationVerificationRequestPayload**](VerifyWebAuthnAuthenticationVerificationRequestPayload.md) |  | 

## Example

```python
from py_logto.models.verify_web_authn_authentication_verification_request import VerifyWebAuthnAuthenticationVerificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyWebAuthnAuthenticationVerificationRequest from a JSON string
verify_web_authn_authentication_verification_request_instance = VerifyWebAuthnAuthenticationVerificationRequest.from_json(json)
# print the JSON string representation of the object
print(VerifyWebAuthnAuthenticationVerificationRequest.to_json())

# convert the object into a dict
verify_web_authn_authentication_verification_request_dict = verify_web_authn_authentication_verification_request_instance.to_dict()
# create an instance of VerifyWebAuthnAuthenticationVerificationRequest from a dict
verify_web_authn_authentication_verification_request_from_dict = VerifyWebAuthnAuthenticationVerificationRequest.from_dict(verify_web_authn_authentication_verification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


