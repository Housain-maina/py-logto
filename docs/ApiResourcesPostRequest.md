# ApiResourcesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the resource. | 
**indicator** | **str** | The unique resource indicator. Should be a valid URI. | 
**access_token_ttl** | **float** | The access token TTL in seconds. It affects the &#x60;exp&#x60; claim of the access token granted for this resource. | [optional] [default to 3600]

## Example

```python
from py_logto.models.api_resources_post_request import ApiResourcesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResourcesPostRequest from a JSON string
api_resources_post_request_instance = ApiResourcesPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiResourcesPostRequest.to_json())

# convert the object into a dict
api_resources_post_request_dict = api_resources_post_request_instance.to_dict()
# create an instance of ApiResourcesPostRequest from a dict
api_resources_post_request_from_dict = ApiResourcesPostRequest.from_dict(api_resources_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


