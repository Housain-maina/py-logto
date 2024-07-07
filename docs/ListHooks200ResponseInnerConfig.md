# ListHooks200ResponseInnerConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**headers** | **Dict[str, str]** |  | [optional] 
**retries** | **float** |  | [optional] 

## Example

```python
from py_logto.models.list_hooks200_response_inner_config import ListHooks200ResponseInnerConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ListHooks200ResponseInnerConfig from a JSON string
list_hooks200_response_inner_config_instance = ListHooks200ResponseInnerConfig.from_json(json)
# print the JSON string representation of the object
print(ListHooks200ResponseInnerConfig.to_json())

# convert the object into a dict
list_hooks200_response_inner_config_dict = list_hooks200_response_inner_config_instance.to_dict()
# create an instance of ListHooks200ResponseInnerConfig from a dict
list_hooks200_response_inner_config_from_dict = ListHooks200ResponseInnerConfig.from_dict(list_hooks200_response_inner_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


