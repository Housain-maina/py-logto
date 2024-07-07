# UpdateConnectorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | The connector config object that will be passed to the connector. The config object should be compatible with the connector factory. | [optional] 
**metadata** | [**UpdateConnectorRequestMetadata**](UpdateConnectorRequestMetadata.md) |  | [optional] 
**sync_profile** | **bool** | Whether to sync user profile from the identity provider to Logto at each sign-in. If &#x60;false&#x60;, the user profile will only be synced when the user is created. | [optional] 

## Example

```python
from py_logto.models.update_connector_request import UpdateConnectorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateConnectorRequest from a JSON string
update_connector_request_instance = UpdateConnectorRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateConnectorRequest.to_json())

# convert the object into a dict
update_connector_request_dict = update_connector_request_instance.to_dict()
# create an instance of UpdateConnectorRequest from a dict
update_connector_request_from_dict = UpdateConnectorRequest.from_dict(update_connector_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


