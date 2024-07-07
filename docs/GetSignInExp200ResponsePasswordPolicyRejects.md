# GetSignInExp200ResponsePasswordPolicyRejects


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pwned** | **bool** |  | [default to True]
**repetition_and_sequence** | **bool** |  | [default to True]
**user_info** | **bool** |  | [default to True]
**words** | **List[str]** |  | [default to []]

## Example

```python
from py_logto.models.get_sign_in_exp200_response_password_policy_rejects import GetSignInExp200ResponsePasswordPolicyRejects

# TODO update the JSON string below
json = "{}"
# create an instance of GetSignInExp200ResponsePasswordPolicyRejects from a JSON string
get_sign_in_exp200_response_password_policy_rejects_instance = GetSignInExp200ResponsePasswordPolicyRejects.from_json(json)
# print the JSON string representation of the object
print(GetSignInExp200ResponsePasswordPolicyRejects.to_json())

# convert the object into a dict
get_sign_in_exp200_response_password_policy_rejects_dict = get_sign_in_exp200_response_password_policy_rejects_instance.to_dict()
# create an instance of GetSignInExp200ResponsePasswordPolicyRejects from a dict
get_sign_in_exp200_response_password_policy_rejects_from_dict = GetSignInExp200ResponsePasswordPolicyRejects.from_dict(get_sign_in_exp200_response_password_policy_rejects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


