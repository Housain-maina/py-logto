# CreateVerificationByPasswordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | The password of the user. | 

## Example

```python
from py_logto.models.create_verification_by_password_request import CreateVerificationByPasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVerificationByPasswordRequest from a JSON string
create_verification_by_password_request_instance = CreateVerificationByPasswordRequest.from_json(json)
# print the JSON string representation of the object
print(CreateVerificationByPasswordRequest.to_json())

# convert the object into a dict
create_verification_by_password_request_dict = create_verification_by_password_request_instance.to_dict()
# create an instance of CreateVerificationByPasswordRequest from a dict
create_verification_by_password_request_from_dict = CreateVerificationByPasswordRequest.from_dict(create_verification_by_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


