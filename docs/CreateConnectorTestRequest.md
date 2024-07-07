# CreateConnectorTestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** | Phone number to send test message to. If this is set, email will be ignored. | [optional] 
**email** | **str** | Email address to send test message to. If phone is set, this will be ignored. | [optional] 
**config** | **object** | Connector configuration object for testing. | 

## Example

```python
from py_logto.models.create_connector_test_request import CreateConnectorTestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConnectorTestRequest from a JSON string
create_connector_test_request_instance = CreateConnectorTestRequest.from_json(json)
# print the JSON string representation of the object
print(CreateConnectorTestRequest.to_json())

# convert the object into a dict
create_connector_test_request_dict = create_connector_test_request_instance.to_dict()
# create an instance of CreateConnectorTestRequest from a dict
create_connector_test_request_from_dict = CreateConnectorTestRequest.from_dict(create_connector_test_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


