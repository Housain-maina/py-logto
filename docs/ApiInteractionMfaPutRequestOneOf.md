# ApiInteractionMfaPutRequestOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | 
**raw_id** | **str** |  | 
**authenticator_attachment** | **str** |  | [optional] 
**client_extension_results** | [**VerifyWebAuthnRegistrationVerificationRequestPayloadClientExtensionResults**](VerifyWebAuthnRegistrationVerificationRequestPayloadClientExtensionResults.md) |  | 
**response** | [**VerifyWebAuthnAuthenticationVerificationRequestPayloadResponse**](VerifyWebAuthnAuthenticationVerificationRequestPayloadResponse.md) |  | 

## Example

```python
from py_logto.models.api_interaction_mfa_put_request_one_of import ApiInteractionMfaPutRequestOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInteractionMfaPutRequestOneOf from a JSON string
api_interaction_mfa_put_request_one_of_instance = ApiInteractionMfaPutRequestOneOf.from_json(json)
# print the JSON string representation of the object
print(ApiInteractionMfaPutRequestOneOf.to_json())

# convert the object into a dict
api_interaction_mfa_put_request_one_of_dict = api_interaction_mfa_put_request_one_of_instance.to_dict()
# create an instance of ApiInteractionMfaPutRequestOneOf from a dict
api_interaction_mfa_put_request_one_of_from_dict = ApiInteractionMfaPutRequestOneOf.from_dict(api_interaction_mfa_put_request_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


