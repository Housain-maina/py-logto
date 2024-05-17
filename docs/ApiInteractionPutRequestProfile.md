# ApiInteractionPutRequestProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**connector_id** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from py_logto.models.api_interaction_put_request_profile import ApiInteractionPutRequestProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInteractionPutRequestProfile from a JSON string
api_interaction_put_request_profile_instance = ApiInteractionPutRequestProfile.from_json(json)
# print the JSON string representation of the object
print(ApiInteractionPutRequestProfile.to_json())

# convert the object into a dict
api_interaction_put_request_profile_dict = api_interaction_put_request_profile_instance.to_dict()
# create an instance of ApiInteractionPutRequestProfile from a dict
api_interaction_put_request_profile_from_dict = ApiInteractionPutRequestProfile.from_dict(api_interaction_put_request_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


