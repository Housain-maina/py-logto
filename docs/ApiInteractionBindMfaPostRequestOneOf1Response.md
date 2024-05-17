# ApiInteractionBindMfaPostRequestOneOf1Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_data_json** | **str** |  | 
**attestation_object** | **str** |  | 
**authenticator_data** | **str** |  | [optional] 
**transports** | **List[str]** |  | [optional] 
**public_key_algorithm** | **float** |  | [optional] 
**public_key** | **str** |  | [optional] 

## Example

```python
from py_logto.models.api_interaction_bind_mfa_post_request_one_of1_response import ApiInteractionBindMfaPostRequestOneOf1Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInteractionBindMfaPostRequestOneOf1Response from a JSON string
api_interaction_bind_mfa_post_request_one_of1_response_instance = ApiInteractionBindMfaPostRequestOneOf1Response.from_json(json)
# print the JSON string representation of the object
print(ApiInteractionBindMfaPostRequestOneOf1Response.to_json())

# convert the object into a dict
api_interaction_bind_mfa_post_request_one_of1_response_dict = api_interaction_bind_mfa_post_request_one_of1_response_instance.to_dict()
# create an instance of ApiInteractionBindMfaPostRequestOneOf1Response from a dict
api_interaction_bind_mfa_post_request_one_of1_response_from_dict = ApiInteractionBindMfaPostRequestOneOf1Response.from_dict(api_interaction_bind_mfa_post_request_one_of1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


