# ApiVerificationCodesVerifyPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**verification_code** | **str** |  | 
**phone** | **str** |  | 

## Example

```python
from py_logto.models.api_verification_codes_verify_post_request import ApiVerificationCodesVerifyPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiVerificationCodesVerifyPostRequest from a JSON string
api_verification_codes_verify_post_request_instance = ApiVerificationCodesVerifyPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiVerificationCodesVerifyPostRequest.to_json())

# convert the object into a dict
api_verification_codes_verify_post_request_dict = api_verification_codes_verify_post_request_instance.to_dict()
# create an instance of ApiVerificationCodesVerifyPostRequest from a dict
api_verification_codes_verify_post_request_from_dict = ApiVerificationCodesVerifyPostRequest.from_dict(api_verification_codes_verify_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


