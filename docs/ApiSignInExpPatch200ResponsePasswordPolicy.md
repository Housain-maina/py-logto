# ApiSignInExpPatch200ResponsePasswordPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**length** | [**ApiSignInExpGet200ResponsePasswordPolicyLength**](ApiSignInExpGet200ResponsePasswordPolicyLength.md) |  | [optional] 
**character_types** | [**ApiSignInExpGet200ResponsePasswordPolicyCharacterTypes**](ApiSignInExpGet200ResponsePasswordPolicyCharacterTypes.md) |  | [optional] 
**rejects** | [**ApiSignInExpGet200ResponsePasswordPolicyRejects**](ApiSignInExpGet200ResponsePasswordPolicyRejects.md) |  | [optional] 

## Example

```python
from py_logto.models.api_sign_in_exp_patch200_response_password_policy import ApiSignInExpPatch200ResponsePasswordPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSignInExpPatch200ResponsePasswordPolicy from a JSON string
api_sign_in_exp_patch200_response_password_policy_instance = ApiSignInExpPatch200ResponsePasswordPolicy.from_json(json)
# print the JSON string representation of the object
print(ApiSignInExpPatch200ResponsePasswordPolicy.to_json())

# convert the object into a dict
api_sign_in_exp_patch200_response_password_policy_dict = api_sign_in_exp_patch200_response_password_policy_instance.to_dict()
# create an instance of ApiSignInExpPatch200ResponsePasswordPolicy from a dict
api_sign_in_exp_patch200_response_password_policy_from_dict = ApiSignInExpPatch200ResponsePasswordPolicy.from_dict(api_sign_in_exp_patch200_response_password_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


