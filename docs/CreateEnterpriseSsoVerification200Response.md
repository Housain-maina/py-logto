# CreateEnterpriseSsoVerification200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_uri** | **str** | The SSO authorization URI. | 
**verification_id** | **str** | The unique verification ID of the newly created EnterpriseSSO verification record. The &#x60;verificationId&#x60; is required when verifying the SSO authorization response. | 

## Example

```python
from py_logto.models.create_enterprise_sso_verification200_response import CreateEnterpriseSsoVerification200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEnterpriseSsoVerification200Response from a JSON string
create_enterprise_sso_verification200_response_instance = CreateEnterpriseSsoVerification200Response.from_json(json)
# print the JSON string representation of the object
print(CreateEnterpriseSsoVerification200Response.to_json())

# convert the object into a dict
create_enterprise_sso_verification200_response_dict = create_enterprise_sso_verification200_response_instance.to_dict()
# create an instance of CreateEnterpriseSsoVerification200Response from a dict
create_enterprise_sso_verification200_response_from_dict = CreateEnterpriseSsoVerification200Response.from_dict(create_enterprise_sso_verification200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


