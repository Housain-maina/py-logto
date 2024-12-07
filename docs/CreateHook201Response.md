# CreateHook201Response


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
from py_logto.models.create_hook201_response import CreateHook201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHook201Response from a JSON string
create_hook201_response_instance = CreateHook201Response.from_json(json)
# print the JSON string representation of the object
print(CreateHook201Response.to_json())

# convert the object into a dict
create_hook201_response_dict = create_hook201_response_instance.to_dict()
# create an instance of CreateHook201Response from a dict
create_hook201_response_from_dict = CreateHook201Response.from_dict(create_hook201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


