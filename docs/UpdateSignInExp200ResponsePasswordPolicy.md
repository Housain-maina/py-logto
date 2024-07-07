# UpdateSignInExp200ResponsePasswordPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**length** | [**GetSignInExp200ResponsePasswordPolicyLength**](GetSignInExp200ResponsePasswordPolicyLength.md) |  | [optional] 
**character_types** | [**GetSignInExp200ResponsePasswordPolicyCharacterTypes**](GetSignInExp200ResponsePasswordPolicyCharacterTypes.md) |  | [optional] 
**rejects** | [**GetSignInExp200ResponsePasswordPolicyRejects**](GetSignInExp200ResponsePasswordPolicyRejects.md) |  | [optional] 

## Example

```python
from py_logto.models.update_sign_in_exp200_response_password_policy import UpdateSignInExp200ResponsePasswordPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSignInExp200ResponsePasswordPolicy from a JSON string
update_sign_in_exp200_response_password_policy_instance = UpdateSignInExp200ResponsePasswordPolicy.from_json(json)
# print the JSON string representation of the object
print(UpdateSignInExp200ResponsePasswordPolicy.to_json())

# convert the object into a dict
update_sign_in_exp200_response_password_policy_dict = update_sign_in_exp200_response_password_policy_instance.to_dict()
# create an instance of UpdateSignInExp200ResponsePasswordPolicy from a dict
update_sign_in_exp200_response_password_policy_from_dict = UpdateSignInExp200ResponsePasswordPolicy.from_dict(update_sign_in_exp200_response_password_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


