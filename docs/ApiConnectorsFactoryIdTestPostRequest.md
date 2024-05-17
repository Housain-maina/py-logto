# ApiConnectorsFactoryIdTestPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** | Phone number to send test message to. If this is set, email will be ignored. | [optional] 
**email** | **str** | Email address to send test message to. If phone is set, this will be ignored. | [optional] 
**config** | **object** | Connector configuration object for testing. | 

## Example

```python
from py_logto.models.api_connectors_factory_id_test_post_request import ApiConnectorsFactoryIdTestPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiConnectorsFactoryIdTestPostRequest from a JSON string
api_connectors_factory_id_test_post_request_instance = ApiConnectorsFactoryIdTestPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiConnectorsFactoryIdTestPostRequest.to_json())

# convert the object into a dict
api_connectors_factory_id_test_post_request_dict = api_connectors_factory_id_test_post_request_instance.to_dict()
# create an instance of ApiConnectorsFactoryIdTestPostRequest from a dict
api_connectors_factory_id_test_post_request_from_dict = ApiConnectorsFactoryIdTestPostRequest.from_dict(api_connectors_factory_id_test_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


