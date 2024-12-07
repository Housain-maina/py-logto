# CreateNewPasswordIdentityVerificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | [**CreateNewPasswordIdentityVerificationRequestIdentifier**](CreateNewPasswordIdentityVerificationRequestIdentifier.md) |  | 
**password** | **str** | The new user password. (A password digest will be created and stored securely in the verification record.) | 

## Example

```python
from py_logto.models.create_new_password_identity_verification_request import CreateNewPasswordIdentityVerificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNewPasswordIdentityVerificationRequest from a JSON string
create_new_password_identity_verification_request_instance = CreateNewPasswordIdentityVerificationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateNewPasswordIdentityVerificationRequest.to_json())

# convert the object into a dict
create_new_password_identity_verification_request_dict = create_new_password_identity_verification_request_instance.to_dict()
# create an instance of CreateNewPasswordIdentityVerificationRequest from a dict
create_new_password_identity_verification_request_from_dict = CreateNewPasswordIdentityVerificationRequest.from_dict(create_new_password_identity_verification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


