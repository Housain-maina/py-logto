# CreateUserMfaVerificationRequestOneOf2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of MFA verification to create. | 
**secret** | **str** | The secret for the MFA verification, if not provided, a new secret will be generated. | [optional] 

## Example

```python
from py_logto.models.create_user_mfa_verification_request_one_of2 import CreateUserMfaVerificationRequestOneOf2

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserMfaVerificationRequestOneOf2 from a JSON string
create_user_mfa_verification_request_one_of2_instance = CreateUserMfaVerificationRequestOneOf2.from_json(json)
# print the JSON string representation of the object
print(CreateUserMfaVerificationRequestOneOf2.to_json())

# convert the object into a dict
create_user_mfa_verification_request_one_of2_dict = create_user_mfa_verification_request_one_of2_instance.to_dict()
# create an instance of CreateUserMfaVerificationRequestOneOf2 from a dict
create_user_mfa_verification_request_one_of2_from_dict = CreateUserMfaVerificationRequestOneOf2.from_dict(create_user_mfa_verification_request_one_of2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


