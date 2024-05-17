# ApiConnectorsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | The connector config object that will be passed to the connector. The config object should be compatible with the connector factory. | [optional] 
**connector_id** | **str** | The connector factory ID for creating the connector. | 
**metadata** | [**ApiConnectorsPostRequestMetadata**](ApiConnectorsPostRequestMetadata.md) |  | [optional] 
**sync_profile** | **bool** | Whether to sync user profile from the identity provider to Logto at each sign-in. If &#x60;false&#x60;, the user profile will only be synced when the user is created. | [optional] 
**id** | **str** | The unique ID for the connector. If not provided, a random ID will be generated. | [optional] 

## Example

```python
from py_logto.models.api_connectors_post_request import ApiConnectorsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiConnectorsPostRequest from a JSON string
api_connectors_post_request_instance = ApiConnectorsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiConnectorsPostRequest.to_json())

# convert the object into a dict
api_connectors_post_request_dict = api_connectors_post_request_instance.to_dict()
# create an instance of ApiConnectorsPostRequest from a dict
api_connectors_post_request_from_dict = ApiConnectorsPostRequest.from_dict(api_connectors_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


