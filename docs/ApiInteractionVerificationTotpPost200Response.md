# ApiInteractionVerificationTotpPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret** | **str** |  | 
**secret_qr_code** | **str** |  | 

## Example

```python
from py_logto.models.api_interaction_verification_totp_post200_response import ApiInteractionVerificationTotpPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInteractionVerificationTotpPost200Response from a JSON string
api_interaction_verification_totp_post200_response_instance = ApiInteractionVerificationTotpPost200Response.from_json(json)
# print the JSON string representation of the object
print(ApiInteractionVerificationTotpPost200Response.to_json())

# convert the object into a dict
api_interaction_verification_totp_post200_response_dict = api_interaction_verification_totp_post200_response_instance.to_dict()
# create an instance of ApiInteractionVerificationTotpPost200Response from a dict
api_interaction_verification_totp_post200_response_from_dict = ApiInteractionVerificationTotpPost200Response.from_dict(api_interaction_verification_totp_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


