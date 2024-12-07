# CheckPasswordWithDefaultSignInExperienceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | The password to check. | 
**user_id** | **str** | The user ID to check the password for. It is required if rejects user info is enabled in the password policy. | [optional] 

## Example

```python
from py_logto.models.check_password_with_default_sign_in_experience_request import CheckPasswordWithDefaultSignInExperienceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CheckPasswordWithDefaultSignInExperienceRequest from a JSON string
check_password_with_default_sign_in_experience_request_instance = CheckPasswordWithDefaultSignInExperienceRequest.from_json(json)
# print the JSON string representation of the object
print(CheckPasswordWithDefaultSignInExperienceRequest.to_json())

# convert the object into a dict
check_password_with_default_sign_in_experience_request_dict = check_password_with_default_sign_in_experience_request_instance.to_dict()
# create an instance of CheckPasswordWithDefaultSignInExperienceRequest from a dict
check_password_with_default_sign_in_experience_request_from_dict = CheckPasswordWithDefaultSignInExperienceRequest.from_dict(check_password_with_default_sign_in_experience_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


