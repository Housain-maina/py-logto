# ApiSignInExpPatchRequestLanguageInfo

Control the language detection policy for the sign-in page.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_detect** | **bool** |  | 
**fallback_language** | **str** |  | 

## Example

```python
from py_logto.models.api_sign_in_exp_patch_request_language_info import ApiSignInExpPatchRequestLanguageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSignInExpPatchRequestLanguageInfo from a JSON string
api_sign_in_exp_patch_request_language_info_instance = ApiSignInExpPatchRequestLanguageInfo.from_json(json)
# print the JSON string representation of the object
print(ApiSignInExpPatchRequestLanguageInfo.to_json())

# convert the object into a dict
api_sign_in_exp_patch_request_language_info_dict = api_sign_in_exp_patch_request_language_info_instance.to_dict()
# create an instance of ApiSignInExpPatchRequestLanguageInfo from a dict
api_sign_in_exp_patch_request_language_info_from_dict = ApiSignInExpPatchRequestLanguageInfo.from_dict(api_sign_in_exp_patch_request_language_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


