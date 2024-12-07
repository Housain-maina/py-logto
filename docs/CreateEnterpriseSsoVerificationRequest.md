# CreateEnterpriseSsoVerificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The state parameter to pass to the SSO connector. | 
**redirect_uri** | **str** | The URI to redirect the user after the SSO authorization is completed. | 

## Example

```python
from py_logto.models.create_enterprise_sso_verification_request import CreateEnterpriseSsoVerificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEnterpriseSsoVerificationRequest from a JSON string
create_enterprise_sso_verification_request_instance = CreateEnterpriseSsoVerificationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateEnterpriseSsoVerificationRequest.to_json())

# convert the object into a dict
create_enterprise_sso_verification_request_dict = create_enterprise_sso_verification_request_instance.to_dict()
# create an instance of CreateEnterpriseSsoVerificationRequest from a dict
create_enterprise_sso_verification_request_from_dict = CreateEnterpriseSsoVerificationRequest.from_dict(create_enterprise_sso_verification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


