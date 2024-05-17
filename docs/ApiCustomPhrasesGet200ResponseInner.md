# ApiCustomPhrasesGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**language_tag** | **str** |  | 
**translation** | [**TranslationObject**](TranslationObject.md) |  | 

## Example

```python
from py_logto.models.api_custom_phrases_get200_response_inner import ApiCustomPhrasesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCustomPhrasesGet200ResponseInner from a JSON string
api_custom_phrases_get200_response_inner_instance = ApiCustomPhrasesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ApiCustomPhrasesGet200ResponseInner.to_json())

# convert the object into a dict
api_custom_phrases_get200_response_inner_dict = api_custom_phrases_get200_response_inner_instance.to_dict()
# create an instance of ApiCustomPhrasesGet200ResponseInner from a dict
api_custom_phrases_get200_response_inner_from_dict = ApiCustomPhrasesGet200ResponseInner.from_dict(api_custom_phrases_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


