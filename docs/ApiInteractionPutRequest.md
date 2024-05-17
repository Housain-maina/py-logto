# ApiInteractionPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **str** |  | 
**identifier** | [**ApiInteractionPutRequestIdentifier**](ApiInteractionPutRequestIdentifier.md) |  | [optional] 
**profile** | [**ApiInteractionPutRequestProfile**](ApiInteractionPutRequestProfile.md) |  | [optional] 

## Example

```python
from py_logto.models.api_interaction_put_request import ApiInteractionPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInteractionPutRequest from a JSON string
api_interaction_put_request_instance = ApiInteractionPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiInteractionPutRequest.to_json())

# convert the object into a dict
api_interaction_put_request_dict = api_interaction_put_request_instance.to_dict()
# create an instance of ApiInteractionPutRequest from a dict
api_interaction_put_request_from_dict = ApiInteractionPutRequest.from_dict(api_interaction_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


