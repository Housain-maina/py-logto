# CreateNewPasswordIdentityVerificationRequestIdentifier

The unique user identifier.  <br/> Currently, only `username` is accepted. For `email` or `phone` registration, a `CodeVerification` record must be created and used to verify the user's email or phone number identifier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from py_logto.models.create_new_password_identity_verification_request_identifier import CreateNewPasswordIdentityVerificationRequestIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNewPasswordIdentityVerificationRequestIdentifier from a JSON string
create_new_password_identity_verification_request_identifier_instance = CreateNewPasswordIdentityVerificationRequestIdentifier.from_json(json)
# print the JSON string representation of the object
print(CreateNewPasswordIdentityVerificationRequestIdentifier.to_json())

# convert the object into a dict
create_new_password_identity_verification_request_identifier_dict = create_new_password_identity_verification_request_identifier_instance.to_dict()
# create an instance of CreateNewPasswordIdentityVerificationRequestIdentifier from a dict
create_new_password_identity_verification_request_identifier_from_dict = CreateNewPasswordIdentityVerificationRequestIdentifier.from_dict(create_new_password_identity_verification_request_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


