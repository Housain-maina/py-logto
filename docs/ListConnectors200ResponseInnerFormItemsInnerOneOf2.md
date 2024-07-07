# ListConnectors200ResponseInnerFormItemsInnerOneOf2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**key** | **str** |  | 
**label** | **str** |  | 
**placeholder** | **str** |  | [optional] 
**required** | **bool** |  | [optional] 
**default_value** | **object** |  | [optional] 
**show_conditions** | [**List[ListConnectors200ResponseInnerFormItemsInnerOneOfShowConditionsInner]**](ListConnectors200ResponseInnerFormItemsInnerOneOfShowConditionsInner.md) |  | [optional] 
**description** | **str** |  | [optional] 
**tooltip** | **str** |  | [optional] 
**is_confidential** | **bool** |  | [optional] 

## Example

```python
from py_logto.models.list_connectors200_response_inner_form_items_inner_one_of2 import ListConnectors200ResponseInnerFormItemsInnerOneOf2

# TODO update the JSON string below
json = "{}"
# create an instance of ListConnectors200ResponseInnerFormItemsInnerOneOf2 from a JSON string
list_connectors200_response_inner_form_items_inner_one_of2_instance = ListConnectors200ResponseInnerFormItemsInnerOneOf2.from_json(json)
# print the JSON string representation of the object
print(ListConnectors200ResponseInnerFormItemsInnerOneOf2.to_json())

# convert the object into a dict
list_connectors200_response_inner_form_items_inner_one_of2_dict = list_connectors200_response_inner_form_items_inner_one_of2_instance.to_dict()
# create an instance of ListConnectors200ResponseInnerFormItemsInnerOneOf2 from a dict
list_connectors200_response_inner_form_items_inner_one_of2_from_dict = ListConnectors200ResponseInnerFormItemsInnerOneOf2.from_dict(list_connectors200_response_inner_form_items_inner_one_of2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


