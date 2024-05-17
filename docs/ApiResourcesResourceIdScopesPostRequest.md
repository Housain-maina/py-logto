# ApiResourcesResourceIdScopesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the scope. It should be unique for the resource. | 
**description** | **str** |  | [optional] 

## Example

```python
from py_logto.models.api_resources_resource_id_scopes_post_request import ApiResourcesResourceIdScopesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResourcesResourceIdScopesPostRequest from a JSON string
api_resources_resource_id_scopes_post_request_instance = ApiResourcesResourceIdScopesPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiResourcesResourceIdScopesPostRequest.to_json())

# convert the object into a dict
api_resources_resource_id_scopes_post_request_dict = api_resources_resource_id_scopes_post_request_instance.to_dict()
# create an instance of ApiResourcesResourceIdScopesPostRequest from a dict
api_resources_resource_id_scopes_post_request_from_dict = ApiResourcesResourceIdScopesPostRequest.from_dict(api_resources_resource_id_scopes_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


