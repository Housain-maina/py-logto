# GetSignInExp200ResponseMfa

MFA settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**factors** | **List[str]** |  | 
**policy** | **str** |  | 

## Example

```python
from py_logto.models.get_sign_in_exp200_response_mfa import GetSignInExp200ResponseMfa

# TODO update the JSON string below
json = "{}"
# create an instance of GetSignInExp200ResponseMfa from a JSON string
get_sign_in_exp200_response_mfa_instance = GetSignInExp200ResponseMfa.from_json(json)
# print the JSON string representation of the object
print(GetSignInExp200ResponseMfa.to_json())

# convert the object into a dict
get_sign_in_exp200_response_mfa_dict = get_sign_in_exp200_response_mfa_instance.to_dict()
# create an instance of GetSignInExp200ResponseMfa from a dict
get_sign_in_exp200_response_mfa_from_dict = GetSignInExp200ResponseMfa.from_dict(get_sign_in_exp200_response_mfa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


