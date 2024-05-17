# ApiConnectorsGet200ResponseInnerFormItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**select_items** | [**List[ApiConnectorsGet200ResponseInnerFormItemsInnerOneOfSelectItemsInner]**](ApiConnectorsGet200ResponseInnerFormItemsInnerOneOfSelectItemsInner.md) |  | 
**key** | **str** |  | 
**label** | **str** |  | 
**placeholder** | **str** |  | [optional] 
**required** | **bool** |  | [optional] 
**default_value** | **object** |  | [optional] 
**show_conditions** | [**List[ApiConnectorsGet200ResponseInnerFormItemsInnerOneOfShowConditionsInner]**](ApiConnectorsGet200ResponseInnerFormItemsInnerOneOfShowConditionsInner.md) |  | [optional] 
**description** | **str** |  | [optional] 
**tooltip** | **str** |  | [optional] 
**is_confidential** | **bool** |  | [optional] 

## Example

```python
from py_logto.models.api_connectors_get200_response_inner_form_items_inner import ApiConnectorsGet200ResponseInnerFormItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiConnectorsGet200ResponseInnerFormItemsInner from a JSON string
api_connectors_get200_response_inner_form_items_inner_instance = ApiConnectorsGet200ResponseInnerFormItemsInner.from_json(json)
# print the JSON string representation of the object
print(ApiConnectorsGet200ResponseInnerFormItemsInner.to_json())

# convert the object into a dict
api_connectors_get200_response_inner_form_items_inner_dict = api_connectors_get200_response_inner_form_items_inner_instance.to_dict()
# create an instance of ApiConnectorsGet200ResponseInnerFormItemsInner from a dict
api_connectors_get200_response_inner_form_items_inner_from_dict = ApiConnectorsGet200ResponseInnerFormItemsInner.from_dict(api_connectors_get200_response_inner_form_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


