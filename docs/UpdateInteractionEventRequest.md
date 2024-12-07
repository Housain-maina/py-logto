# UpdateInteractionEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interaction_event** | **str** | The type of the interaction event. Only &#x60;SignIn&#x60; and &#x60;Register&#x60; are supported. | 

## Example

```python
from py_logto.models.update_interaction_event_request import UpdateInteractionEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInteractionEventRequest from a JSON string
update_interaction_event_request_instance = UpdateInteractionEventRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateInteractionEventRequest.to_json())

# convert the object into a dict
update_interaction_event_request_dict = update_interaction_event_request_instance.to_dict()
# create an instance of UpdateInteractionEventRequest from a dict
update_interaction_event_request_from_dict = UpdateInteractionEventRequest.from_dict(update_interaction_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


