# UpdateSignInExpRequestSignIn

Sign-in method settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**methods** | [**List[GetSignInExp200ResponseSignInMethodsInner]**](GetSignInExp200ResponseSignInMethodsInner.md) |  | 

## Example

```python
from py_logto.models.update_sign_in_exp_request_sign_in import UpdateSignInExpRequestSignIn

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSignInExpRequestSignIn from a JSON string
update_sign_in_exp_request_sign_in_instance = UpdateSignInExpRequestSignIn.from_json(json)
# print the JSON string representation of the object
print(UpdateSignInExpRequestSignIn.to_json())

# convert the object into a dict
update_sign_in_exp_request_sign_in_dict = update_sign_in_exp_request_sign_in_instance.to_dict()
# create an instance of UpdateSignInExpRequestSignIn from a dict
update_sign_in_exp_request_sign_in_from_dict = UpdateSignInExpRequestSignIn.from_dict(update_sign_in_exp_request_sign_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


