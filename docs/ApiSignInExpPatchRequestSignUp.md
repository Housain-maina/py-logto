# ApiSignInExpPatchRequestSignUp

Sign-up method settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | **List[str]** | Specify allowed identifiers when signing-up. | 
**password** | **bool** | Whether the user is required to set a password when signing-up. | 
**verify** | **bool** | Whether the user is required to verify their email/phone when signing-up. | 

## Example

```python
from py_logto.models.api_sign_in_exp_patch_request_sign_up import ApiSignInExpPatchRequestSignUp

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSignInExpPatchRequestSignUp from a JSON string
api_sign_in_exp_patch_request_sign_up_instance = ApiSignInExpPatchRequestSignUp.from_json(json)
# print the JSON string representation of the object
print(ApiSignInExpPatchRequestSignUp.to_json())

# convert the object into a dict
api_sign_in_exp_patch_request_sign_up_dict = api_sign_in_exp_patch_request_sign_up_instance.to_dict()
# create an instance of ApiSignInExpPatchRequestSignUp from a dict
api_sign_in_exp_patch_request_sign_up_from_dict = ApiSignInExpPatchRequestSignUp.from_dict(api_sign_in_exp_patch_request_sign_up_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


