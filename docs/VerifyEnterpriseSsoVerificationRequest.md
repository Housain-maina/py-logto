# VerifyEnterpriseSsoVerificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_data** | **object** | Arbitrary data returned by the SSO provider to complete the verification process. | 
**verification_id** | **str** | The ID of the EnterpriseSSO verification record. | 

## Example

```python
from py_logto.models.verify_enterprise_sso_verification_request import VerifyEnterpriseSsoVerificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyEnterpriseSsoVerificationRequest from a JSON string
verify_enterprise_sso_verification_request_instance = VerifyEnterpriseSsoVerificationRequest.from_json(json)
# print the JSON string representation of the object
print(VerifyEnterpriseSsoVerificationRequest.to_json())

# convert the object into a dict
verify_enterprise_sso_verification_request_dict = verify_enterprise_sso_verification_request_instance.to_dict()
# create an instance of VerifyEnterpriseSsoVerificationRequest from a dict
verify_enterprise_sso_verification_request_from_dict = VerifyEnterpriseSsoVerificationRequest.from_dict(verify_enterprise_sso_verification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


