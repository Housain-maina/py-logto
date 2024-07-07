# CreateConnectorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | The connector config object that will be passed to the connector. The config object should be compatible with the connector factory. | [optional] 
**connector_id** | **str** | The connector factory ID for creating the connector. | 
**metadata** | [**CreateConnectorRequestMetadata**](CreateConnectorRequestMetadata.md) |  | [optional] 
**sync_profile** | **bool** | Whether to sync user profile from the identity provider to Logto at each sign-in. If &#x60;false&#x60;, the user profile will only be synced when the user is created. | [optional] 
**id** | **str** | The unique ID for the connector. If not provided, a random ID will be generated. | [optional] 

## Example

```python
from py_logto.models.create_connector_request import CreateConnectorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConnectorRequest from a JSON string
create_connector_request_instance = CreateConnectorRequest.from_json(json)
# print the JSON string representation of the object
print(CreateConnectorRequest.to_json())

# convert the object into a dict
create_connector_request_dict = create_connector_request_instance.to_dict()
# create an instance of CreateConnectorRequest from a dict
create_connector_request_from_dict = CreateConnectorRequest.from_dict(create_connector_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


