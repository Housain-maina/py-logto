# CreatePasswordVerificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | [**CreatePasswordVerificationRequestIdentifier**](CreatePasswordVerificationRequestIdentifier.md) |  | 
**password** | **str** | The user password. | 

## Example

```python
from py_logto.models.create_password_verification_request import CreatePasswordVerificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePasswordVerificationRequest from a JSON string
create_password_verification_request_instance = CreatePasswordVerificationRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePasswordVerificationRequest.to_json())

# convert the object into a dict
create_password_verification_request_dict = create_password_verification_request_instance.to_dict()
# create an instance of CreatePasswordVerificationRequest from a dict
create_password_verification_request_from_dict = CreatePasswordVerificationRequest.from_dict(create_password_verification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


