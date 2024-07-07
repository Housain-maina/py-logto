# CreateUserMfaVerification200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**secret** | **str** |  | 
**secret_qr_code** | **str** |  | 

## Example

```python
from py_logto.models.create_user_mfa_verification200_response_one_of import CreateUserMfaVerification200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserMfaVerification200ResponseOneOf from a JSON string
create_user_mfa_verification200_response_one_of_instance = CreateUserMfaVerification200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(CreateUserMfaVerification200ResponseOneOf.to_json())

# convert the object into a dict
create_user_mfa_verification200_response_one_of_dict = create_user_mfa_verification200_response_one_of_instance.to_dict()
# create an instance of CreateUserMfaVerification200ResponseOneOf from a dict
create_user_mfa_verification200_response_one_of_from_dict = CreateUserMfaVerification200ResponseOneOf.from_dict(create_user_mfa_verification200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


