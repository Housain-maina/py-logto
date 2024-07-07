# CreateConnectorRequestMetadata

Custom connector metadata, will be used to overwrite the default connector factory metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** |  | [optional] 
**name** | **object** | Validator function | [optional] 
**logo** | **str** |  | [optional] 
**logo_dark** | **str** |  | [optional] 

## Example

```python
from py_logto.models.create_connector_request_metadata import CreateConnectorRequestMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConnectorRequestMetadata from a JSON string
create_connector_request_metadata_instance = CreateConnectorRequestMetadata.from_json(json)
# print the JSON string representation of the object
print(CreateConnectorRequestMetadata.to_json())

# convert the object into a dict
create_connector_request_metadata_dict = create_connector_request_metadata_instance.to_dict()
# create an instance of CreateConnectorRequestMetadata from a dict
create_connector_request_metadata_from_dict = CreateConnectorRequestMetadata.from_dict(create_connector_request_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


