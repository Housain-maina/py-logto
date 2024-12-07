# CreateUserMfaVerificationRequestOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**secret** | **str** |  | [optional] 

## Example

```python
from py_logto.models.create_user_mfa_verification_request_one_of import CreateUserMfaVerificationRequestOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserMfaVerificationRequestOneOf from a JSON string
create_user_mfa_verification_request_one_of_instance = CreateUserMfaVerificationRequestOneOf.from_json(json)
# print the JSON string representation of the object
print(CreateUserMfaVerificationRequestOneOf.to_json())

# convert the object into a dict
create_user_mfa_verification_request_one_of_dict = create_user_mfa_verification_request_one_of_instance.to_dict()
# create an instance of CreateUserMfaVerificationRequestOneOf from a dict
create_user_mfa_verification_request_one_of_from_dict = CreateUserMfaVerificationRequestOneOf.from_dict(create_user_mfa_verification_request_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


