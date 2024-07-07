# UpdateSignInExpRequestColor

Specify the primary branding color for the sign-in page (both light/dark mode).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_color** | **str** |  | 
**is_dark_mode_enabled** | **bool** |  | 
**dark_primary_color** | **str** |  | 

## Example

```python
from py_logto.models.update_sign_in_exp_request_color import UpdateSignInExpRequestColor

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSignInExpRequestColor from a JSON string
update_sign_in_exp_request_color_instance = UpdateSignInExpRequestColor.from_json(json)
# print the JSON string representation of the object
print(UpdateSignInExpRequestColor.to_json())

# convert the object into a dict
update_sign_in_exp_request_color_dict = update_sign_in_exp_request_color_instance.to_dict()
# create an instance of UpdateSignInExpRequestColor from a dict
update_sign_in_exp_request_color_from_dict = UpdateSignInExpRequestColor.from_dict(update_sign_in_exp_request_color_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


