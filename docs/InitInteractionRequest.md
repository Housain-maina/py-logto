# InitInteractionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interaction_event** | **str** |  | 

## Example

```python
from py_logto.models.init_interaction_request import InitInteractionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InitInteractionRequest from a JSON string
init_interaction_request_instance = InitInteractionRequest.from_json(json)
# print the JSON string representation of the object
print(InitInteractionRequest.to_json())

# convert the object into a dict
init_interaction_request_dict = init_interaction_request_instance.to_dict()
# create an instance of InitInteractionRequest from a dict
init_interaction_request_from_dict = InitInteractionRequest.from_dict(init_interaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


