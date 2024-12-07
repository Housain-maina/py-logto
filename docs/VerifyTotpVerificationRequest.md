# VerifyTotpVerificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The TOTP code to be verified. | 
**verification_id** | **str** | The verification ID of the newly created TOTP secret. This ID is required to verify a newly created TOTP secret that needs to be bound to the user account. If not provided, the API will create a new TOTP verification record and verify the code against the user&#39;s existing TOTP secret. | [optional] 

## Example

```python
from py_logto.models.verify_totp_verification_request import VerifyTotpVerificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyTotpVerificationRequest from a JSON string
verify_totp_verification_request_instance = VerifyTotpVerificationRequest.from_json(json)
# print the JSON string representation of the object
print(VerifyTotpVerificationRequest.to_json())

# convert the object into a dict
verify_totp_verification_request_dict = verify_totp_verification_request_instance.to_dict()
# create an instance of VerifyTotpVerificationRequest from a dict
verify_totp_verification_request_from_dict = VerifyTotpVerificationRequest.from_dict(verify_totp_verification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


