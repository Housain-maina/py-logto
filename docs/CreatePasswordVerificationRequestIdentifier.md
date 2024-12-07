# CreatePasswordVerificationRequestIdentifier

The unique identifier of the user that will be used to identify the user along with the provided password.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from py_logto.models.create_password_verification_request_identifier import CreatePasswordVerificationRequestIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePasswordVerificationRequestIdentifier from a JSON string
create_password_verification_request_identifier_instance = CreatePasswordVerificationRequestIdentifier.from_json(json)
# print the JSON string representation of the object
print(CreatePasswordVerificationRequestIdentifier.to_json())

# convert the object into a dict
create_password_verification_request_identifier_dict = create_password_verification_request_identifier_instance.to_dict()
# create an instance of CreatePasswordVerificationRequestIdentifier from a dict
create_password_verification_request_identifier_from_dict = CreatePasswordVerificationRequestIdentifier.from_dict(create_password_verification_request_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


