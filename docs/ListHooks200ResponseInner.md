# ListHooks200ResponseInner


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
**execution_stats** | [**ListHooks200ResponseInnerExecutionStats**](ListHooks200ResponseInnerExecutionStats.md) |  | [optional] 

## Example

```python
from py_logto.models.list_hooks200_response_inner import ListHooks200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListHooks200ResponseInner from a JSON string
list_hooks200_response_inner_instance = ListHooks200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListHooks200ResponseInner.to_json())

# convert the object into a dict
list_hooks200_response_inner_dict = list_hooks200_response_inner_instance.to_dict()
# create an instance of ListHooks200ResponseInner from a dict
list_hooks200_response_inner_from_dict = ListHooks200ResponseInner.from_dict(list_hooks200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


