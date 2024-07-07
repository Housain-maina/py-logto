# CreateUserMfaVerification200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**secret** | **str** |  | 
**secret_qr_code** | **str** |  | 
**codes** | **List[str]** |  | 

## Example

```python
from py_logto.models.create_user_mfa_verification200_response import CreateUserMfaVerification200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserMfaVerification200Response from a JSON string
create_user_mfa_verification200_response_instance = CreateUserMfaVerification200Response.from_json(json)
# print the JSON string representation of the object
print(CreateUserMfaVerification200Response.to_json())

# convert the object into a dict
create_user_mfa_verification200_response_dict = create_user_mfa_verification200_response_instance.to_dict()
# create an instance of CreateUserMfaVerification200Response from a dict
create_user_mfa_verification200_response_from_dict = CreateUserMfaVerification200Response.from_dict(create_user_mfa_verification200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


