# GetSignInExp200ResponseSignIn

Sign-in method settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**methods** | [**List[GetSignInExp200ResponseSignInMethodsInner]**](GetSignInExp200ResponseSignInMethodsInner.md) |  | 

## Example

```python
from py_logto.models.get_sign_in_exp200_response_sign_in import GetSignInExp200ResponseSignIn

# TODO update the JSON string below
json = "{}"
# create an instance of GetSignInExp200ResponseSignIn from a JSON string
get_sign_in_exp200_response_sign_in_instance = GetSignInExp200ResponseSignIn.from_json(json)
# print the JSON string representation of the object
print(GetSignInExp200ResponseSignIn.to_json())

# convert the object into a dict
get_sign_in_exp200_response_sign_in_dict = get_sign_in_exp200_response_sign_in_instance.to_dict()
# create an instance of GetSignInExp200ResponseSignIn from a dict
get_sign_in_exp200_response_sign_in_from_dict = GetSignInExp200ResponseSignIn.from_dict(get_sign_in_exp200_response_sign_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


