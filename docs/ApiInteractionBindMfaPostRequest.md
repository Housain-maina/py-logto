# ApiInteractionBindMfaPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**code** | **str** |  | 
**id** | **str** |  | 
**raw_id** | **str** |  | 
**response** | [**ApiInteractionBindMfaPostRequestOneOf1Response**](ApiInteractionBindMfaPostRequestOneOf1Response.md) |  | 
**authenticator_attachment** | **str** |  | [optional] 
**client_extension_results** | [**ApiInteractionBindMfaPostRequestOneOf1ClientExtensionResults**](ApiInteractionBindMfaPostRequestOneOf1ClientExtensionResults.md) |  | 

## Example

```python
from py_logto.models.api_interaction_bind_mfa_post_request import ApiInteractionBindMfaPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInteractionBindMfaPostRequest from a JSON string
api_interaction_bind_mfa_post_request_instance = ApiInteractionBindMfaPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiInteractionBindMfaPostRequest.to_json())

# convert the object into a dict
api_interaction_bind_mfa_post_request_dict = api_interaction_bind_mfa_post_request_instance.to_dict()
# create an instance of ApiInteractionBindMfaPostRequest from a dict
api_interaction_bind_mfa_post_request_from_dict = ApiInteractionBindMfaPostRequest.from_dict(api_interaction_bind_mfa_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


