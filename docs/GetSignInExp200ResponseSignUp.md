# GetSignInExp200ResponseSignUp

Sign-up method settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | **List[str]** | Allowed identifiers when signing-up. | 
**password** | **bool** | Whether the user is required to set a password when signing-up. | 
**verify** | **bool** | Whether the user is required to verify their email/phone when signing-up. | 

## Example

```python
from py_logto.models.get_sign_in_exp200_response_sign_up import GetSignInExp200ResponseSignUp

# TODO update the JSON string below
json = "{}"
# create an instance of GetSignInExp200ResponseSignUp from a JSON string
get_sign_in_exp200_response_sign_up_instance = GetSignInExp200ResponseSignUp.from_json(json)
# print the JSON string representation of the object
print(GetSignInExp200ResponseSignUp.to_json())

# convert the object into a dict
get_sign_in_exp200_response_sign_up_dict = get_sign_in_exp200_response_sign_up_instance.to_dict()
# create an instance of GetSignInExp200ResponseSignUp from a dict
get_sign_in_exp200_response_sign_up_from_dict = GetSignInExp200ResponseSignUp.from_dict(get_sign_in_exp200_response_sign_up_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


