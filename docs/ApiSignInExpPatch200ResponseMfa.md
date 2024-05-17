# ApiSignInExpPatch200ResponseMfa


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**factors** | **List[str]** |  | 
**policy** | **str** |  | 

## Example

```python
from py_logto.models.api_sign_in_exp_patch200_response_mfa import ApiSignInExpPatch200ResponseMfa

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSignInExpPatch200ResponseMfa from a JSON string
api_sign_in_exp_patch200_response_mfa_instance = ApiSignInExpPatch200ResponseMfa.from_json(json)
# print the JSON string representation of the object
print(ApiSignInExpPatch200ResponseMfa.to_json())

# convert the object into a dict
api_sign_in_exp_patch200_response_mfa_dict = api_sign_in_exp_patch200_response_mfa_instance.to_dict()
# create an instance of ApiSignInExpPatch200ResponseMfa from a dict
api_sign_in_exp_patch200_response_mfa_from_dict = ApiSignInExpPatch200ResponseMfa.from_dict(api_sign_in_exp_patch200_response_mfa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


