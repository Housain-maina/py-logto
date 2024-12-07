# CreateUserMfaVerificationRequestOneOf3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of MFA verification to create. | 
**codes** | **List[str]** | The backup codes for the MFA verification, if not provided, a new group of backup codes will be generated. | [optional] 

## Example

```python
from py_logto.models.create_user_mfa_verification_request_one_of3 import CreateUserMfaVerificationRequestOneOf3

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserMfaVerificationRequestOneOf3 from a JSON string
create_user_mfa_verification_request_one_of3_instance = CreateUserMfaVerificationRequestOneOf3.from_json(json)
# print the JSON string representation of the object
print(CreateUserMfaVerificationRequestOneOf3.to_json())

# convert the object into a dict
create_user_mfa_verification_request_one_of3_dict = create_user_mfa_verification_request_one_of3_instance.to_dict()
# create an instance of CreateUserMfaVerificationRequestOneOf3 from a dict
create_user_mfa_verification_request_one_of3_from_dict = CreateUserMfaVerificationRequestOneOf3.from_dict(create_user_mfa_verification_request_one_of3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


