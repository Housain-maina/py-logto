# UpdateSignInExpRequestLanguageInfo

Control the language detection policy for the sign-in page.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_detect** | **bool** |  | 
**fallback_language** | **str** |  | 

## Example

```python
from py_logto.models.update_sign_in_exp_request_language_info import UpdateSignInExpRequestLanguageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSignInExpRequestLanguageInfo from a JSON string
update_sign_in_exp_request_language_info_instance = UpdateSignInExpRequestLanguageInfo.from_json(json)
# print the JSON string representation of the object
print(UpdateSignInExpRequestLanguageInfo.to_json())

# convert the object into a dict
update_sign_in_exp_request_language_info_dict = update_sign_in_exp_request_language_info_instance.to_dict()
# create an instance of UpdateSignInExpRequestLanguageInfo from a dict
update_sign_in_exp_request_language_info_from_dict = UpdateSignInExpRequestLanguageInfo.from_dict(update_sign_in_exp_request_language_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


