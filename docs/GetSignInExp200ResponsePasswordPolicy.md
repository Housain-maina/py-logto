# GetSignInExp200ResponsePasswordPolicy

Password policies to adjust the password strength requirements.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**length** | [**GetSignInExp200ResponsePasswordPolicyLength**](GetSignInExp200ResponsePasswordPolicyLength.md) |  | [optional] 
**character_types** | [**GetSignInExp200ResponsePasswordPolicyCharacterTypes**](GetSignInExp200ResponsePasswordPolicyCharacterTypes.md) |  | [optional] 
**rejects** | [**GetSignInExp200ResponsePasswordPolicyRejects**](GetSignInExp200ResponsePasswordPolicyRejects.md) |  | [optional] 

## Example

```python
from py_logto.models.get_sign_in_exp200_response_password_policy import GetSignInExp200ResponsePasswordPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of GetSignInExp200ResponsePasswordPolicy from a JSON string
get_sign_in_exp200_response_password_policy_instance = GetSignInExp200ResponsePasswordPolicy.from_json(json)
# print the JSON string representation of the object
print(GetSignInExp200ResponsePasswordPolicy.to_json())

# convert the object into a dict
get_sign_in_exp200_response_password_policy_dict = get_sign_in_exp200_response_password_policy_instance.to_dict()
# create an instance of GetSignInExp200ResponsePasswordPolicy from a dict
get_sign_in_exp200_response_password_policy_from_dict = GetSignInExp200ResponsePasswordPolicy.from_dict(get_sign_in_exp200_response_password_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


