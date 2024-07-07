# UpdateConnectorRequestMetadata

Custom connector metadata, will be used to overwrite the default connector metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** |  | [optional] 
**name** | **object** | Validator function | [optional] 
**logo** | **str** |  | [optional] 
**logo_dark** | **str** |  | [optional] 

## Example

```python
from py_logto.models.update_connector_request_metadata import UpdateConnectorRequestMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateConnectorRequestMetadata from a JSON string
update_connector_request_metadata_instance = UpdateConnectorRequestMetadata.from_json(json)
# print the JSON string representation of the object
print(UpdateConnectorRequestMetadata.to_json())

# convert the object into a dict
update_connector_request_metadata_dict = update_connector_request_metadata_instance.to_dict()
# create an instance of UpdateConnectorRequestMetadata from a dict
update_connector_request_metadata_from_dict = UpdateConnectorRequestMetadata.from_dict(update_connector_request_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


