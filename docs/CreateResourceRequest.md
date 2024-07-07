# CreateResourceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 
**name** | **str** | The name of the resource. | 
**indicator** | **str** | The unique resource indicator. Should be a valid URI. | 
**access_token_ttl** | **float** | The access token TTL in seconds. It affects the &#x60;exp&#x60; claim of the access token granted for this resource. | [optional] [default to 3600]

## Example

```python
from py_logto.models.create_resource_request import CreateResourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateResourceRequest from a JSON string
create_resource_request_instance = CreateResourceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateResourceRequest.to_json())

# convert the object into a dict
create_resource_request_dict = create_resource_request_instance.to_dict()
# create an instance of CreateResourceRequest from a dict
create_resource_request_from_dict = CreateResourceRequest.from_dict(create_resource_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


