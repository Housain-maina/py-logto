# VerifyVerificationCodeVerification200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_id** | **str** | he unique ID of the verification record. Required for user identification via the &#x60;Identification&#x60; API or to bind the identifier to the user&#39;s account via the &#x60;Profile&#x60; API. | 

## Example

```python
from py_logto.models.verify_verification_code_verification200_response import VerifyVerificationCodeVerification200Response

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyVerificationCodeVerification200Response from a JSON string
verify_verification_code_verification200_response_instance = VerifyVerificationCodeVerification200Response.from_json(json)
# print the JSON string representation of the object
print(VerifyVerificationCodeVerification200Response.to_json())

# convert the object into a dict
verify_verification_code_verification200_response_dict = verify_verification_code_verification200_response_instance.to_dict()
# create an instance of VerifyVerificationCodeVerification200Response from a dict
verify_verification_code_verification200_response_from_dict = VerifyVerificationCodeVerification200Response.from_dict(verify_verification_code_verification200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


