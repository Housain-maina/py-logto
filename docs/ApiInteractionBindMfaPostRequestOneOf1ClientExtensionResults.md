# ApiInteractionBindMfaPostRequestOneOf1ClientExtensionResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appid** | **bool** |  | [optional] 
**crep_props** | [**ApiInteractionBindMfaPostRequestOneOf1ClientExtensionResultsCrepProps**](ApiInteractionBindMfaPostRequestOneOf1ClientExtensionResultsCrepProps.md) |  | [optional] 
**hmac_create_secret** | **bool** |  | [optional] 

## Example

```python
from py_logto.models.api_interaction_bind_mfa_post_request_one_of1_client_extension_results import ApiInteractionBindMfaPostRequestOneOf1ClientExtensionResults

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInteractionBindMfaPostRequestOneOf1ClientExtensionResults from a JSON string
api_interaction_bind_mfa_post_request_one_of1_client_extension_results_instance = ApiInteractionBindMfaPostRequestOneOf1ClientExtensionResults.from_json(json)
# print the JSON string representation of the object
print(ApiInteractionBindMfaPostRequestOneOf1ClientExtensionResults.to_json())

# convert the object into a dict
api_interaction_bind_mfa_post_request_one_of1_client_extension_results_dict = api_interaction_bind_mfa_post_request_one_of1_client_extension_results_instance.to_dict()
# create an instance of ApiInteractionBindMfaPostRequestOneOf1ClientExtensionResults from a dict
api_interaction_bind_mfa_post_request_one_of1_client_extension_results_from_dict = ApiInteractionBindMfaPostRequestOneOf1ClientExtensionResults.from_dict(api_interaction_bind_mfa_post_request_one_of1_client_extension_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


