# ApiConnectorsIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | The connector config object that will be passed to the connector. The config object should be compatible with the connector factory. | [optional] 
**metadata** | [**ApiConnectorsIdPatchRequestMetadata**](ApiConnectorsIdPatchRequestMetadata.md) |  | [optional] 
**sync_profile** | **bool** | Whether to sync user profile from the identity provider to Logto at each sign-in. If &#x60;false&#x60;, the user profile will only be synced when the user is created. | [optional] 

## Example

```python
from py_logto.models.api_connectors_id_patch_request import ApiConnectorsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiConnectorsIdPatchRequest from a JSON string
api_connectors_id_patch_request_instance = ApiConnectorsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(ApiConnectorsIdPatchRequest.to_json())

# convert the object into a dict
api_connectors_id_patch_request_dict = api_connectors_id_patch_request_instance.to_dict()
# create an instance of ApiConnectorsIdPatchRequest from a dict
api_connectors_id_patch_request_from_dict = ApiConnectorsIdPatchRequest.from_dict(api_connectors_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


