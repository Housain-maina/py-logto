# UpdateSignInExpRequestSignUp

Sign-up method settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | **List[str]** | Specify allowed identifiers when signing-up. | 
**password** | **bool** | Whether the user is required to set a password when signing-up. | 
**verify** | **bool** | Whether the user is required to verify their email/phone when signing-up. | 

## Example

```python
from py_logto.models.update_sign_in_exp_request_sign_up import UpdateSignInExpRequestSignUp

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSignInExpRequestSignUp from a JSON string
update_sign_in_exp_request_sign_up_instance = UpdateSignInExpRequestSignUp.from_json(json)
# print the JSON string representation of the object
print(UpdateSignInExpRequestSignUp.to_json())

# convert the object into a dict
update_sign_in_exp_request_sign_up_dict = update_sign_in_exp_request_sign_up_instance.to_dict()
# create an instance of UpdateSignInExpRequestSignUp from a dict
update_sign_in_exp_request_sign_up_from_dict = UpdateSignInExpRequestSignUp.from_dict(update_sign_in_exp_request_sign_up_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


