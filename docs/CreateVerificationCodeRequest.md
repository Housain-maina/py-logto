# CreateVerificationCodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**phone** | **str** |  | 

## Example

```python
from py_logto.models.create_verification_code_request import CreateVerificationCodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVerificationCodeRequest from a JSON string
create_verification_code_request_instance = CreateVerificationCodeRequest.from_json(json)
# print the JSON string representation of the object
print(CreateVerificationCodeRequest.to_json())

# convert the object into a dict
create_verification_code_request_dict = create_verification_code_request_instance.to_dict()
# create an instance of CreateVerificationCodeRequest from a dict
create_verification_code_request_from_dict = CreateVerificationCodeRequest.from_dict(create_verification_code_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


