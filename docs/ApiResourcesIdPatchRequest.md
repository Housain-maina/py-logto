# ApiResourcesIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The updated name of the resource. | [optional] 
**access_token_ttl** | **float** | The updated access token TTL in seconds. | [optional] 

## Example

```python
from py_logto.models.api_resources_id_patch_request import ApiResourcesIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResourcesIdPatchRequest from a JSON string
api_resources_id_patch_request_instance = ApiResourcesIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(ApiResourcesIdPatchRequest.to_json())

# convert the object into a dict
api_resources_id_patch_request_dict = api_resources_id_patch_request_instance.to_dict()
# create an instance of ApiResourcesIdPatchRequest from a dict
api_resources_id_patch_request_from_dict = ApiResourcesIdPatchRequest.from_dict(api_resources_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


