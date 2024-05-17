# TranslationObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**translation_key** | [**Translation**](Translation.md) |  | [optional] 

## Example

```python
from py_logto.models.translation_object import TranslationObject

# TODO update the JSON string below
json = "{}"
# create an instance of TranslationObject from a JSON string
translation_object_instance = TranslationObject.from_json(json)
# print the JSON string representation of the object
print(TranslationObject.to_json())

# convert the object into a dict
translation_object_dict = translation_object_instance.to_dict()
# create an instance of TranslationObject from a dict
translation_object_from_dict = TranslationObject.from_dict(translation_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


