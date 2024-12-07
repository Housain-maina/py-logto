# VerifyWebAuthnAuthenticationVerificationRequestPayloadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_data_json** | **str** |  | 
**authenticator_data** | **str** |  | 
**signature** | **str** |  | 
**user_handle** | **str** |  | [optional] 

## Example

```python
from py_logto.models.verify_web_authn_authentication_verification_request_payload_response import VerifyWebAuthnAuthenticationVerificationRequestPayloadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyWebAuthnAuthenticationVerificationRequestPayloadResponse from a JSON string
verify_web_authn_authentication_verification_request_payload_response_instance = VerifyWebAuthnAuthenticationVerificationRequestPayloadResponse.from_json(json)
# print the JSON string representation of the object
print(VerifyWebAuthnAuthenticationVerificationRequestPayloadResponse.to_json())

# convert the object into a dict
verify_web_authn_authentication_verification_request_payload_response_dict = verify_web_authn_authentication_verification_request_payload_response_instance.to_dict()
# create an instance of VerifyWebAuthnAuthenticationVerificationRequestPayloadResponse from a dict
verify_web_authn_authentication_verification_request_payload_response_from_dict = VerifyWebAuthnAuthenticationVerificationRequestPayloadResponse.from_dict(verify_web_authn_authentication_verification_request_payload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


