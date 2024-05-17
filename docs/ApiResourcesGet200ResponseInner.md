# ApiResourcesGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**indicator** | **str** |  | 
**is_default** | **bool** |  | 
**access_token_ttl** | **float** |  | 
**scopes** | [**List[ApiResourcesGet200ResponseInnerScopesInner]**](ApiResourcesGet200ResponseInnerScopesInner.md) |  | [optional] 

## Example

```python
from py_logto.models.api_resources_get200_response_inner import ApiResourcesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResourcesGet200ResponseInner from a JSON string
api_resources_get200_response_inner_instance = ApiResourcesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ApiResourcesGet200ResponseInner.to_json())

# convert the object into a dict
api_resources_get200_response_inner_dict = api_resources_get200_response_inner_instance.to_dict()
# create an instance of ApiResourcesGet200ResponseInner from a dict
api_resources_get200_response_inner_from_dict = ApiResourcesGet200ResponseInner.from_dict(api_resources_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


