# GetSignInExp200ResponseLanguageInfo

The language detection policy for the sign-in page.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_detect** | **bool** |  | 
**fallback_language** | **str** |  | 

## Example

```python
from py_logto.models.get_sign_in_exp200_response_language_info import GetSignInExp200ResponseLanguageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GetSignInExp200ResponseLanguageInfo from a JSON string
get_sign_in_exp200_response_language_info_instance = GetSignInExp200ResponseLanguageInfo.from_json(json)
# print the JSON string representation of the object
print(GetSignInExp200ResponseLanguageInfo.to_json())

# convert the object into a dict
get_sign_in_exp200_response_language_info_dict = get_sign_in_exp200_response_language_info_instance.to_dict()
# create an instance of GetSignInExp200ResponseLanguageInfo from a dict
get_sign_in_exp200_response_language_info_from_dict = GetSignInExp200ResponseLanguageInfo.from_dict(get_sign_in_exp200_response_language_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


