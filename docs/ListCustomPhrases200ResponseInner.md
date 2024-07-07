# ListCustomPhrases200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**id** | **str** |  | 
**language_tag** | **str** |  | 
**translation** | [**TranslationObject**](TranslationObject.md) |  | 

## Example

```python
from py_logto.models.list_custom_phrases200_response_inner import ListCustomPhrases200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListCustomPhrases200ResponseInner from a JSON string
list_custom_phrases200_response_inner_instance = ListCustomPhrases200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListCustomPhrases200ResponseInner.to_json())

# convert the object into a dict
list_custom_phrases200_response_inner_dict = list_custom_phrases200_response_inner_instance.to_dict()
# create an instance of ListCustomPhrases200ResponseInner from a dict
list_custom_phrases200_response_inner_from_dict = ListCustomPhrases200ResponseInner.from_dict(list_custom_phrases200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


