# VerifyWebAuthnAuthenticationVerification200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_id** | **str** | The unique verification ID of the WebAuthn authentication verification record. | 

## Example

```python
from py_logto.models.verify_web_authn_authentication_verification200_response import VerifyWebAuthnAuthenticationVerification200Response

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyWebAuthnAuthenticationVerification200Response from a JSON string
verify_web_authn_authentication_verification200_response_instance = VerifyWebAuthnAuthenticationVerification200Response.from_json(json)
# print the JSON string representation of the object
print(VerifyWebAuthnAuthenticationVerification200Response.to_json())

# convert the object into a dict
verify_web_authn_authentication_verification200_response_dict = verify_web_authn_authentication_verification200_response_instance.to_dict()
# create an instance of VerifyWebAuthnAuthenticationVerification200Response from a dict
verify_web_authn_authentication_verification200_response_from_dict = VerifyWebAuthnAuthenticationVerification200Response.from_dict(verify_web_authn_authentication_verification200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


