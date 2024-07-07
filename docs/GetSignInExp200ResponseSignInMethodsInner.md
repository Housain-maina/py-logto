# GetSignInExp200ResponseSignInMethodsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | 
**password** | **bool** |  | 
**verification_code** | **bool** |  | 
**is_password_primary** | **bool** |  | 

## Example

```python
from py_logto.models.get_sign_in_exp200_response_sign_in_methods_inner import GetSignInExp200ResponseSignInMethodsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSignInExp200ResponseSignInMethodsInner from a JSON string
get_sign_in_exp200_response_sign_in_methods_inner_instance = GetSignInExp200ResponseSignInMethodsInner.from_json(json)
# print the JSON string representation of the object
print(GetSignInExp200ResponseSignInMethodsInner.to_json())

# convert the object into a dict
get_sign_in_exp200_response_sign_in_methods_inner_dict = get_sign_in_exp200_response_sign_in_methods_inner_instance.to_dict()
# create an instance of GetSignInExp200ResponseSignInMethodsInner from a dict
get_sign_in_exp200_response_sign_in_methods_inner_from_dict = GetSignInExp200ResponseSignInMethodsInner.from_dict(get_sign_in_exp200_response_sign_in_methods_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


