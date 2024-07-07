# ListResources200ResponseInnerScopesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**id** | **str** |  | 
**resource_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**created_at** | **float** |  | 

## Example

```python
from py_logto.models.list_resources200_response_inner_scopes_inner import ListResources200ResponseInnerScopesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListResources200ResponseInnerScopesInner from a JSON string
list_resources200_response_inner_scopes_inner_instance = ListResources200ResponseInnerScopesInner.from_json(json)
# print the JSON string representation of the object
print(ListResources200ResponseInnerScopesInner.to_json())

# convert the object into a dict
list_resources200_response_inner_scopes_inner_dict = list_resources200_response_inner_scopes_inner_instance.to_dict()
# create an instance of ListResources200ResponseInnerScopesInner from a dict
list_resources200_response_inner_scopes_inner_from_dict = ListResources200ResponseInnerScopesInner.from_dict(list_resources200_response_inner_scopes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


