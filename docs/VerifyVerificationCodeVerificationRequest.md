# VerifyVerificationCodeVerificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | [**VerifyVerificationCodeVerificationRequestIdentifier**](VerifyVerificationCodeVerificationRequestIdentifier.md) |  | 
**verification_id** | **str** | The verification ID of the CodeVerification record. | 
**code** | **str** | The verification code to be verified. | 

## Example

```python
from py_logto.models.verify_verification_code_verification_request import VerifyVerificationCodeVerificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyVerificationCodeVerificationRequest from a JSON string
verify_verification_code_verification_request_instance = VerifyVerificationCodeVerificationRequest.from_json(json)
# print the JSON string representation of the object
print(VerifyVerificationCodeVerificationRequest.to_json())

# convert the object into a dict
verify_verification_code_verification_request_dict = verify_verification_code_verification_request_instance.to_dict()
# create an instance of VerifyVerificationCodeVerificationRequest from a dict
verify_verification_code_verification_request_from_dict = VerifyVerificationCodeVerificationRequest.from_dict(verify_verification_code_verification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


