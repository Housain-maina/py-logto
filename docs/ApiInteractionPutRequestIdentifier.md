# ApiInteractionPutRequestIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**password** | **str** |  | 
**email** | **str** |  | 
**phone** | **str** |  | 
**verification_code** | **str** |  | 
**connector_id** | **str** |  | 
**connector_data** | **object** | arbitrary | 

## Example

```python
from py_logto.models.api_interaction_put_request_identifier import ApiInteractionPutRequestIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInteractionPutRequestIdentifier from a JSON string
api_interaction_put_request_identifier_instance = ApiInteractionPutRequestIdentifier.from_json(json)
# print the JSON string representation of the object
print(ApiInteractionPutRequestIdentifier.to_json())

# convert the object into a dict
api_interaction_put_request_identifier_dict = api_interaction_put_request_identifier_instance.to_dict()
# create an instance of ApiInteractionPutRequestIdentifier from a dict
api_interaction_put_request_identifier_from_dict = ApiInteractionPutRequestIdentifier.from_dict(api_interaction_put_request_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


