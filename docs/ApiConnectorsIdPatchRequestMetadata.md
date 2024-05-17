# ApiConnectorsIdPatchRequestMetadata

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
from py_logto.models.api_connectors_id_patch_request_metadata import ApiConnectorsIdPatchRequestMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ApiConnectorsIdPatchRequestMetadata from a JSON string
api_connectors_id_patch_request_metadata_instance = ApiConnectorsIdPatchRequestMetadata.from_json(json)
# print the JSON string representation of the object
print(ApiConnectorsIdPatchRequestMetadata.to_json())

# convert the object into a dict
api_connectors_id_patch_request_metadata_dict = api_connectors_id_patch_request_metadata_instance.to_dict()
# create an instance of ApiConnectorsIdPatchRequestMetadata from a dict
api_connectors_id_patch_request_metadata_from_dict = ApiConnectorsIdPatchRequestMetadata.from_dict(api_connectors_id_patch_request_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


