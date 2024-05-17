# ApiHooksGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**event** | **str** |  | 
**events** | **List[str]** |  | 
**config** | [**ApiHooksGet200ResponseInnerConfig**](ApiHooksGet200ResponseInnerConfig.md) |  | 
**signing_key** | **str** |  | 
**enabled** | **bool** |  | 
**created_at** | **float** |  | 
**execution_stats** | [**ApiHooksGet200ResponseInnerExecutionStats**](ApiHooksGet200ResponseInnerExecutionStats.md) |  | [optional] 

## Example

```python
from py_logto.models.api_hooks_get200_response_inner import ApiHooksGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiHooksGet200ResponseInner from a JSON string
api_hooks_get200_response_inner_instance = ApiHooksGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ApiHooksGet200ResponseInner.to_json())

# convert the object into a dict
api_hooks_get200_response_inner_dict = api_hooks_get200_response_inner_instance.to_dict()
# create an instance of ApiHooksGet200ResponseInner from a dict
api_hooks_get200_response_inner_from_dict = ApiHooksGet200ResponseInner.from_dict(api_hooks_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


