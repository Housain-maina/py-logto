# CreateNewPasswordIdentityVerification200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_id** | **str** | The unique verification ID of the newly created NewPasswordIdentity verification record. The &#x60;verificationId&#x60; is required when creating a new user account via the &#x60;Identification&#x60; API. | 

## Example

```python
from py_logto.models.create_new_password_identity_verification200_response import CreateNewPasswordIdentityVerification200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNewPasswordIdentityVerification200Response from a JSON string
create_new_password_identity_verification200_response_instance = CreateNewPasswordIdentityVerification200Response.from_json(json)
# print the JSON string representation of the object
print(CreateNewPasswordIdentityVerification200Response.to_json())

# convert the object into a dict
create_new_password_identity_verification200_response_dict = create_new_password_identity_verification200_response_instance.to_dict()
# create an instance of CreateNewPasswordIdentityVerification200Response from a dict
create_new_password_identity_verification200_response_from_dict = CreateNewPasswordIdentityVerification200Response.from_dict(create_new_password_identity_verification200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


