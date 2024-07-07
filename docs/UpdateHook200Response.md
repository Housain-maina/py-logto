# UpdateHook200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**event** | **str** |  | 
**events** | **List[str]** |  | 
**config** | [**ListHooks200ResponseInnerConfig**](ListHooks200ResponseInnerConfig.md) |  | 
**signing_key** | **str** |  | 
**enabled** | **bool** |  | 
**created_at** | **float** |  | 

## Example

```python
from py_logto.models.update_hook200_response import UpdateHook200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateHook200Response from a JSON string
update_hook200_response_instance = UpdateHook200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateHook200Response.to_json())

# convert the object into a dict
update_hook200_response_dict = update_hook200_response_instance.to_dict()
# create an instance of UpdateHook200Response from a dict
update_hook200_response_from_dict = UpdateHook200Response.from_dict(update_hook200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


