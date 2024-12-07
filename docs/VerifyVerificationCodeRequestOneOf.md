# VerifyVerificationCodeRequestOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**verification_code** | **str** |  | 

## Example

```python
from py_logto.models.verify_verification_code_request_one_of import VerifyVerificationCodeRequestOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyVerificationCodeRequestOneOf from a JSON string
verify_verification_code_request_one_of_instance = VerifyVerificationCodeRequestOneOf.from_json(json)
# print the JSON string representation of the object
print(VerifyVerificationCodeRequestOneOf.to_json())

# convert the object into a dict
verify_verification_code_request_one_of_dict = verify_verification_code_request_one_of_instance.to_dict()
# create an instance of VerifyVerificationCodeRequestOneOf from a dict
verify_verification_code_request_one_of_from_dict = VerifyVerificationCodeRequestOneOf.from_dict(verify_verification_code_request_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


