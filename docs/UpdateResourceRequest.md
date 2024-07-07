# UpdateResourceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 
**name** | **str** | The updated name of the resource. | [optional] 
**access_token_ttl** | **float** | The updated access token TTL in seconds. | [optional] 

## Example

```python
from py_logto.models.update_resource_request import UpdateResourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateResourceRequest from a JSON string
update_resource_request_instance = UpdateResourceRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateResourceRequest.to_json())

# convert the object into a dict
update_resource_request_dict = update_resource_request_instance.to_dict()
# create an instance of UpdateResourceRequest from a dict
update_resource_request_from_dict = UpdateResourceRequest.from_dict(update_resource_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


