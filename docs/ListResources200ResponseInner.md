# ListResources200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**indicator** | **str** |  | 
**is_default** | **bool** |  | 
**access_token_ttl** | **float** |  | 
**scopes** | [**List[ListResources200ResponseInnerScopesInner]**](ListResources200ResponseInnerScopesInner.md) |  | [optional] 

## Example

```python
from py_logto.models.list_resources200_response_inner import ListResources200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListResources200ResponseInner from a JSON string
list_resources200_response_inner_instance = ListResources200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListResources200ResponseInner.to_json())

# convert the object into a dict
list_resources200_response_inner_dict = list_resources200_response_inner_instance.to_dict()
# create an instance of ListResources200ResponseInner from a dict
list_resources200_response_inner_from_dict = ListResources200ResponseInner.from_dict(list_resources200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


