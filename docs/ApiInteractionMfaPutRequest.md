# ApiInteractionMfaPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**code** | **str** |  | 
**id** | **str** |  | 
**raw_id** | **str** |  | 
**authenticator_attachment** | **str** |  | [optional] 
**client_extension_results** | [**ApiInteractionBindMfaPostRequestOneOf1ClientExtensionResults**](ApiInteractionBindMfaPostRequestOneOf1ClientExtensionResults.md) |  | 
**response** | [**ApiInteractionMfaPutRequestOneOfResponse**](ApiInteractionMfaPutRequestOneOfResponse.md) |  | 

## Example

```python
from py_logto.models.api_interaction_mfa_put_request import ApiInteractionMfaPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInteractionMfaPutRequest from a JSON string
api_interaction_mfa_put_request_instance = ApiInteractionMfaPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiInteractionMfaPutRequest.to_json())

# convert the object into a dict
api_interaction_mfa_put_request_dict = api_interaction_mfa_put_request_instance.to_dict()
# create an instance of ApiInteractionMfaPutRequest from a dict
api_interaction_mfa_put_request_from_dict = ApiInteractionMfaPutRequest.from_dict(api_interaction_mfa_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


