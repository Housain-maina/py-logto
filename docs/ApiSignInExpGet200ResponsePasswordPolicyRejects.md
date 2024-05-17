# ApiSignInExpGet200ResponsePasswordPolicyRejects


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pwned** | **bool** |  | [default to True]
**repetition_and_sequence** | **bool** |  | [default to True]
**user_info** | **bool** |  | [default to True]
**words** | **List[str]** |  | [default to []]

## Example

```python
from py_logto.models.api_sign_in_exp_get200_response_password_policy_rejects import ApiSignInExpGet200ResponsePasswordPolicyRejects

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSignInExpGet200ResponsePasswordPolicyRejects from a JSON string
api_sign_in_exp_get200_response_password_policy_rejects_instance = ApiSignInExpGet200ResponsePasswordPolicyRejects.from_json(json)
# print the JSON string representation of the object
print(ApiSignInExpGet200ResponsePasswordPolicyRejects.to_json())

# convert the object into a dict
api_sign_in_exp_get200_response_password_policy_rejects_dict = api_sign_in_exp_get200_response_password_policy_rejects_instance.to_dict()
# create an instance of ApiSignInExpGet200ResponsePasswordPolicyRejects from a dict
api_sign_in_exp_get200_response_password_policy_rejects_from_dict = ApiSignInExpGet200ResponsePasswordPolicyRejects.from_dict(api_sign_in_exp_get200_response_password_policy_rejects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


