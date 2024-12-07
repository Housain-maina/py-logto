# VerifyWebAuthnRegistrationVerificationRequestPayloadClientExtensionResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appid** | **bool** |  | [optional] 
**crep_props** | [**VerifyWebAuthnRegistrationVerificationRequestPayloadClientExtensionResultsCrepProps**](VerifyWebAuthnRegistrationVerificationRequestPayloadClientExtensionResultsCrepProps.md) |  | [optional] 
**hmac_create_secret** | **bool** |  | [optional] 

## Example

```python
from py_logto.models.verify_web_authn_registration_verification_request_payload_client_extension_results import VerifyWebAuthnRegistrationVerificationRequestPayloadClientExtensionResults

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyWebAuthnRegistrationVerificationRequestPayloadClientExtensionResults from a JSON string
verify_web_authn_registration_verification_request_payload_client_extension_results_instance = VerifyWebAuthnRegistrationVerificationRequestPayloadClientExtensionResults.from_json(json)
# print the JSON string representation of the object
print(VerifyWebAuthnRegistrationVerificationRequestPayloadClientExtensionResults.to_json())

# convert the object into a dict
verify_web_authn_registration_verification_request_payload_client_extension_results_dict = verify_web_authn_registration_verification_request_payload_client_extension_results_instance.to_dict()
# create an instance of VerifyWebAuthnRegistrationVerificationRequestPayloadClientExtensionResults from a dict
verify_web_authn_registration_verification_request_payload_client_extension_results_from_dict = VerifyWebAuthnRegistrationVerificationRequestPayloadClientExtensionResults.from_dict(verify_web_authn_registration_verification_request_payload_client_extension_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


