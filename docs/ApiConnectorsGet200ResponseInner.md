# ApiConnectorsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**sync_profile** | **bool** |  | 
**config** | **object** | arbitrary | 
**metadata** | [**ApiConnectorsGet200ResponseInnerMetadata**](ApiConnectorsGet200ResponseInnerMetadata.md) |  | 
**connector_id** | **str** |  | 
**target** | **str** |  | 
**name** | **object** | Validator function | 
**description** | **object** | Validator function | 
**logo** | **str** |  | 
**logo_dark** | **str** |  | 
**readme** | **str** |  | 
**config_template** | **str** |  | [optional] 
**form_items** | [**List[ApiConnectorsGet200ResponseInnerFormItemsInner]**](ApiConnectorsGet200ResponseInnerFormItemsInner.md) |  | [optional] 
**platform** | **str** |  | 
**is_standard** | **bool** |  | [optional] 
**type** | **str** |  | 
**is_demo** | **bool** |  | [optional] 
**extra_info** | **Dict[str, object]** |  | [optional] 
**usage** | **float** |  | [optional] 

## Example

```python
from py_logto.models.api_connectors_get200_response_inner import ApiConnectorsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiConnectorsGet200ResponseInner from a JSON string
api_connectors_get200_response_inner_instance = ApiConnectorsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ApiConnectorsGet200ResponseInner.to_json())

# convert the object into a dict
api_connectors_get200_response_inner_dict = api_connectors_get200_response_inner_instance.to_dict()
# create an instance of ApiConnectorsGet200ResponseInner from a dict
api_connectors_get200_response_inner_from_dict = ApiConnectorsGet200ResponseInner.from_dict(api_connectors_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


