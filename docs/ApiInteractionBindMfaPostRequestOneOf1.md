# ApiInteractionBindMfaPostRequestOneOf1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | 
**raw_id** | **str** |  | 
**response** | [**VerifyWebAuthnRegistrationVerificationRequestPayloadResponse**](VerifyWebAuthnRegistrationVerificationRequestPayloadResponse.md) |  | 
**authenticator_attachment** | **str** |  | [optional] 
**client_extension_results** | [**VerifyWebAuthnRegistrationVerificationRequestPayloadClientExtensionResults**](VerifyWebAuthnRegistrationVerificationRequestPayloadClientExtensionResults.md) |  | 

## Example

```python
from py_logto.models.api_interaction_bind_mfa_post_request_one_of1 import ApiInteractionBindMfaPostRequestOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInteractionBindMfaPostRequestOneOf1 from a JSON string
api_interaction_bind_mfa_post_request_one_of1_instance = ApiInteractionBindMfaPostRequestOneOf1.from_json(json)
# print the JSON string representation of the object
print(ApiInteractionBindMfaPostRequestOneOf1.to_json())

# convert the object into a dict
api_interaction_bind_mfa_post_request_one_of1_dict = api_interaction_bind_mfa_post_request_one_of1_instance.to_dict()
# create an instance of ApiInteractionBindMfaPostRequestOneOf1 from a dict
api_interaction_bind_mfa_post_request_one_of1_from_dict = ApiInteractionBindMfaPostRequestOneOf1.from_dict(api_interaction_bind_mfa_post_request_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


