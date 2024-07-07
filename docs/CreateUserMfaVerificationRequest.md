# CreateUserMfaVerificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**CreateUserMfaVerificationRequestType**](CreateUserMfaVerificationRequestType.md) |  | 

## Example

```python
from py_logto.models.create_user_mfa_verification_request import CreateUserMfaVerificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserMfaVerificationRequest from a JSON string
create_user_mfa_verification_request_instance = CreateUserMfaVerificationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateUserMfaVerificationRequest.to_json())

# convert the object into a dict
create_user_mfa_verification_request_dict = create_user_mfa_verification_request_instance.to_dict()
# create an instance of CreateUserMfaVerificationRequest from a dict
create_user_mfa_verification_request_from_dict = CreateUserMfaVerificationRequest.from_dict(create_user_mfa_verification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


