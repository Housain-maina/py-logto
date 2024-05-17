# ApiSignInExpPatchRequestColor

Specify the primary branding color for the sign-in page (both light/dark mode).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_color** | **str** |  | 
**is_dark_mode_enabled** | **bool** |  | 
**dark_primary_color** | **str** |  | 

## Example

```python
from py_logto.models.api_sign_in_exp_patch_request_color import ApiSignInExpPatchRequestColor

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSignInExpPatchRequestColor from a JSON string
api_sign_in_exp_patch_request_color_instance = ApiSignInExpPatchRequestColor.from_json(json)
# print the JSON string representation of the object
print(ApiSignInExpPatchRequestColor.to_json())

# convert the object into a dict
api_sign_in_exp_patch_request_color_dict = api_sign_in_exp_patch_request_color_instance.to_dict()
# create an instance of ApiSignInExpPatchRequestColor from a dict
api_sign_in_exp_patch_request_color_from_dict = ApiSignInExpPatchRequestColor.from_dict(api_sign_in_exp_patch_request_color_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


