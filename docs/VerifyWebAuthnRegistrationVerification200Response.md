# VerifyWebAuthnRegistrationVerification200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_id** | **str** | The unique verification ID of the WebAuthn registration record. This &#x60;verificationId&#x60; is required to bind the WebAuthn credential to the user account via the &#x60;Profile&#x60; API. | 

## Example

```python
from py_logto.models.verify_web_authn_registration_verification200_response import VerifyWebAuthnRegistrationVerification200Response

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyWebAuthnRegistrationVerification200Response from a JSON string
verify_web_authn_registration_verification200_response_instance = VerifyWebAuthnRegistrationVerification200Response.from_json(json)
# print the JSON string representation of the object
print(VerifyWebAuthnRegistrationVerification200Response.to_json())

# convert the object into a dict
verify_web_authn_registration_verification200_response_dict = verify_web_authn_registration_verification200_response_instance.to_dict()
# create an instance of VerifyWebAuthnRegistrationVerification200Response from a dict
verify_web_authn_registration_verification200_response_from_dict = VerifyWebAuthnRegistrationVerification200Response.from_dict(verify_web_authn_registration_verification200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


