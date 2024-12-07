# VerifyEnterpriseSsoVerification200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_id** | **str** | The current verified EnterpriseSSO verification record ID. This ID is required when identifying the user in the current interaction. | 

## Example

```python
from py_logto.models.verify_enterprise_sso_verification200_response import VerifyEnterpriseSsoVerification200Response

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyEnterpriseSsoVerification200Response from a JSON string
verify_enterprise_sso_verification200_response_instance = VerifyEnterpriseSsoVerification200Response.from_json(json)
# print the JSON string representation of the object
print(VerifyEnterpriseSsoVerification200Response.to_json())

# convert the object into a dict
verify_enterprise_sso_verification200_response_dict = verify_enterprise_sso_verification200_response_instance.to_dict()
# create an instance of VerifyEnterpriseSsoVerification200Response from a dict
verify_enterprise_sso_verification200_response_from_dict = VerifyEnterpriseSsoVerification200Response.from_dict(verify_enterprise_sso_verification200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


