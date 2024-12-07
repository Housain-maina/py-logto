# BindMfaVerificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of MFA. | 
**verification_id** | **str** | The ID of the MFA verification record. | 

## Example

```python
from py_logto.models.bind_mfa_verification_request import BindMfaVerificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BindMfaVerificationRequest from a JSON string
bind_mfa_verification_request_instance = BindMfaVerificationRequest.from_json(json)
# print the JSON string representation of the object
print(BindMfaVerificationRequest.to_json())

# convert the object into a dict
bind_mfa_verification_request_dict = bind_mfa_verification_request_instance.to_dict()
# create an instance of BindMfaVerificationRequest from a dict
bind_mfa_verification_request_from_dict = BindMfaVerificationRequest.from_dict(bind_mfa_verification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


