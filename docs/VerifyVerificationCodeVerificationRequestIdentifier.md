# VerifyVerificationCodeVerificationRequestIdentifier

The identifier (email address or phone number) to verify the code against. Must match the identifier used to send the verification code.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from py_logto.models.verify_verification_code_verification_request_identifier import VerifyVerificationCodeVerificationRequestIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyVerificationCodeVerificationRequestIdentifier from a JSON string
verify_verification_code_verification_request_identifier_instance = VerifyVerificationCodeVerificationRequestIdentifier.from_json(json)
# print the JSON string representation of the object
print(VerifyVerificationCodeVerificationRequestIdentifier.to_json())

# convert the object into a dict
verify_verification_code_verification_request_identifier_dict = verify_verification_code_verification_request_identifier_instance.to_dict()
# create an instance of VerifyVerificationCodeVerificationRequestIdentifier from a dict
verify_verification_code_verification_request_identifier_from_dict = VerifyVerificationCodeVerificationRequestIdentifier.from_dict(verify_verification_code_verification_request_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


