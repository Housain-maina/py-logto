# ApiInteractionMfaPutRequestOneOfResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_data_json** | **str** |  | 
**authenticator_data** | **str** |  | 
**signature** | **str** |  | 
**user_handle** | **str** |  | [optional] 

## Example

```python
from py_logto.models.api_interaction_mfa_put_request_one_of_response import ApiInteractionMfaPutRequestOneOfResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInteractionMfaPutRequestOneOfResponse from a JSON string
api_interaction_mfa_put_request_one_of_response_instance = ApiInteractionMfaPutRequestOneOfResponse.from_json(json)
# print the JSON string representation of the object
print(ApiInteractionMfaPutRequestOneOfResponse.to_json())

# convert the object into a dict
api_interaction_mfa_put_request_one_of_response_dict = api_interaction_mfa_put_request_one_of_response_instance.to_dict()
# create an instance of ApiInteractionMfaPutRequestOneOfResponse from a dict
api_interaction_mfa_put_request_one_of_response_from_dict = ApiInteractionMfaPutRequestOneOfResponse.from_dict(api_interaction_mfa_put_request_one_of_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


