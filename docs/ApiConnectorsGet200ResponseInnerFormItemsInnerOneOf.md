# ApiConnectorsGet200ResponseInnerFormItemsInnerOneOf


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
from py_logto.models.api_connectors_get200_response_inner_form_items_inner_one_of import ApiConnectorsGet200ResponseInnerFormItemsInnerOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of ApiConnectorsGet200ResponseInnerFormItemsInnerOneOf from a JSON string
api_connectors_get200_response_inner_form_items_inner_one_of_instance = ApiConnectorsGet200ResponseInnerFormItemsInnerOneOf.from_json(json)
# print the JSON string representation of the object
print(ApiConnectorsGet200ResponseInnerFormItemsInnerOneOf.to_json())

# convert the object into a dict
api_connectors_get200_response_inner_form_items_inner_one_of_dict = api_connectors_get200_response_inner_form_items_inner_one_of_instance.to_dict()
# create an instance of ApiConnectorsGet200ResponseInnerFormItemsInnerOneOf from a dict
api_connectors_get200_response_inner_form_items_inner_one_of_from_dict = ApiConnectorsGet200ResponseInnerFormItemsInnerOneOf.from_dict(api_connectors_get200_response_inner_form_items_inner_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


