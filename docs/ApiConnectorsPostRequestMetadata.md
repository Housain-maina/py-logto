# ApiConnectorsPostRequestMetadata

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
from py_logto.models.api_connectors_post_request_metadata import ApiConnectorsPostRequestMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ApiConnectorsPostRequestMetadata from a JSON string
api_connectors_post_request_metadata_instance = ApiConnectorsPostRequestMetadata.from_json(json)
# print the JSON string representation of the object
print(ApiConnectorsPostRequestMetadata.to_json())

# convert the object into a dict
api_connectors_post_request_metadata_dict = api_connectors_post_request_metadata_instance.to_dict()
# create an instance of ApiConnectorsPostRequestMetadata from a dict
api_connectors_post_request_metadata_from_dict = ApiConnectorsPostRequestMetadata.from_dict(api_connectors_post_request_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


