# VerifyVerificationCodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**verification_code** | **str** |  | 
**phone** | **str** |  | 

## Example

```python
from py_logto.models.verify_verification_code_request import VerifyVerificationCodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyVerificationCodeRequest from a JSON string
verify_verification_code_request_instance = VerifyVerificationCodeRequest.from_json(json)
# print the JSON string representation of the object
print(VerifyVerificationCodeRequest.to_json())

# convert the object into a dict
verify_verification_code_request_dict = verify_verification_code_request_instance.to_dict()
# create an instance of VerifyVerificationCodeRequest from a dict
verify_verification_code_request_from_dict = VerifyVerificationCodeRequest.from_dict(verify_verification_code_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


