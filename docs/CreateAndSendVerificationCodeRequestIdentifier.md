# CreateAndSendVerificationCodeRequestIdentifier

The identifier (email address or phone number) to send the verification code to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from py_logto.models.create_and_send_verification_code_request_identifier import CreateAndSendVerificationCodeRequestIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAndSendVerificationCodeRequestIdentifier from a JSON string
create_and_send_verification_code_request_identifier_instance = CreateAndSendVerificationCodeRequestIdentifier.from_json(json)
# print the JSON string representation of the object
print(CreateAndSendVerificationCodeRequestIdentifier.to_json())

# convert the object into a dict
create_and_send_verification_code_request_identifier_dict = create_and_send_verification_code_request_identifier_instance.to_dict()
# create an instance of CreateAndSendVerificationCodeRequestIdentifier from a dict
create_and_send_verification_code_request_identifier_from_dict = CreateAndSendVerificationCodeRequestIdentifier.from_dict(create_and_send_verification_code_request_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


