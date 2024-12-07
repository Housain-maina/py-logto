# CreateVerificationByVerificationCodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | [**CreateAndSendVerificationCodeRequestIdentifier**](CreateAndSendVerificationCodeRequestIdentifier.md) |  | 

## Example

```python
from py_logto.models.create_verification_by_verification_code_request import CreateVerificationByVerificationCodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVerificationByVerificationCodeRequest from a JSON string
create_verification_by_verification_code_request_instance = CreateVerificationByVerificationCodeRequest.from_json(json)
# print the JSON string representation of the object
print(CreateVerificationByVerificationCodeRequest.to_json())

# convert the object into a dict
create_verification_by_verification_code_request_dict = create_verification_by_verification_code_request_instance.to_dict()
# create an instance of CreateVerificationByVerificationCodeRequest from a dict
create_verification_by_verification_code_request_from_dict = CreateVerificationByVerificationCodeRequest.from_dict(create_verification_by_verification_code_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


