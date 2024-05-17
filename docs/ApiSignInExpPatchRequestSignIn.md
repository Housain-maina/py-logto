# ApiSignInExpPatchRequestSignIn

Sign-in method settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**methods** | [**List[ApiSignInExpGet200ResponseSignInMethodsInner]**](ApiSignInExpGet200ResponseSignInMethodsInner.md) |  | 

## Example

```python
from py_logto.models.api_sign_in_exp_patch_request_sign_in import ApiSignInExpPatchRequestSignIn

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSignInExpPatchRequestSignIn from a JSON string
api_sign_in_exp_patch_request_sign_in_instance = ApiSignInExpPatchRequestSignIn.from_json(json)
# print the JSON string representation of the object
print(ApiSignInExpPatchRequestSignIn.to_json())

# convert the object into a dict
api_sign_in_exp_patch_request_sign_in_dict = api_sign_in_exp_patch_request_sign_in_instance.to_dict()
# create an instance of ApiSignInExpPatchRequestSignIn from a dict
api_sign_in_exp_patch_request_sign_in_from_dict = ApiSignInExpPatchRequestSignIn.from_dict(api_sign_in_exp_patch_request_sign_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


