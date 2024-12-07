# CheckPasswordWithDefaultSignInExperience200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **bool** |  | 
**issues** | [**List[CheckPasswordWithDefaultSignInExperience200ResponseOneOf1IssuesInner]**](CheckPasswordWithDefaultSignInExperience200ResponseOneOf1IssuesInner.md) |  | 

## Example

```python
from py_logto.models.check_password_with_default_sign_in_experience200_response import CheckPasswordWithDefaultSignInExperience200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CheckPasswordWithDefaultSignInExperience200Response from a JSON string
check_password_with_default_sign_in_experience200_response_instance = CheckPasswordWithDefaultSignInExperience200Response.from_json(json)
# print the JSON string representation of the object
print(CheckPasswordWithDefaultSignInExperience200Response.to_json())

# convert the object into a dict
check_password_with_default_sign_in_experience200_response_dict = check_password_with_default_sign_in_experience200_response_instance.to_dict()
# create an instance of CheckPasswordWithDefaultSignInExperience200Response from a dict
check_password_with_default_sign_in_experience200_response_from_dict = CheckPasswordWithDefaultSignInExperience200Response.from_dict(check_password_with_default_sign_in_experience200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


