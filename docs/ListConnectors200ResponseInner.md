# ListConnectors200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**sync_profile** | **bool** |  | 
**config** | **object** | arbitrary | 
**metadata** | [**ListConnectors200ResponseInnerMetadata**](ListConnectors200ResponseInnerMetadata.md) |  | 
**connector_id** | **str** |  | 
**target** | **str** |  | 
**name** | **object** | Validator function | 
**description** | **object** | Validator function | 
**logo** | **str** |  | 
**logo_dark** | **str** |  | 
**readme** | **str** |  | 
**config_template** | **str** |  | [optional] 
**form_items** | [**List[ListConnectors200ResponseInnerFormItemsInner]**](ListConnectors200ResponseInnerFormItemsInner.md) |  | [optional] 
**custom_data** | **Dict[str, object]** |  | [optional] 
**from_email** | **str** |  | [optional] 
**platform** | **str** |  | 
**is_standard** | **bool** |  | [optional] 
**type** | **str** |  | 
**is_demo** | **bool** |  | [optional] 
**extra_info** | **Dict[str, object]** |  | [optional] 
**usage** | **float** |  | [optional] 

## Example

```python
from py_logto.models.list_connectors200_response_inner import ListConnectors200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListConnectors200ResponseInner from a JSON string
list_connectors200_response_inner_instance = ListConnectors200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListConnectors200ResponseInner.to_json())

# convert the object into a dict
list_connectors200_response_inner_dict = list_connectors200_response_inner_instance.to_dict()
# create an instance of ListConnectors200ResponseInner from a dict
list_connectors200_response_inner_from_dict = ListConnectors200ResponseInner.from_dict(list_connectors200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


