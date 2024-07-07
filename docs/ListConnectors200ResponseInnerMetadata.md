# ListConnectors200ResponseInnerMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** |  | [optional] 
**name** | **object** | Validator function | [optional] 
**logo** | **str** |  | [optional] 
**logo_dark** | **str** |  | [optional] 

## Example

```python
from py_logto.models.list_connectors200_response_inner_metadata import ListConnectors200ResponseInnerMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ListConnectors200ResponseInnerMetadata from a JSON string
list_connectors200_response_inner_metadata_instance = ListConnectors200ResponseInnerMetadata.from_json(json)
# print the JSON string representation of the object
print(ListConnectors200ResponseInnerMetadata.to_json())

# convert the object into a dict
list_connectors200_response_inner_metadata_dict = list_connectors200_response_inner_metadata_instance.to_dict()
# create an instance of ListConnectors200ResponseInnerMetadata from a dict
list_connectors200_response_inner_metadata_from_dict = ListConnectors200ResponseInnerMetadata.from_dict(list_connectors200_response_inner_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


