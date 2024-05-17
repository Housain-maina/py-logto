# ApiUsersUserIdMfaVerificationsPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**secret** | **str** |  | 
**secret_qr_code** | **str** |  | 
**codes** | **List[str]** |  | 

## Example

```python
from py_logto.models.api_users_user_id_mfa_verifications_post200_response import ApiUsersUserIdMfaVerificationsPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiUsersUserIdMfaVerificationsPost200Response from a JSON string
api_users_user_id_mfa_verifications_post200_response_instance = ApiUsersUserIdMfaVerificationsPost200Response.from_json(json)
# print the JSON string representation of the object
print(ApiUsersUserIdMfaVerificationsPost200Response.to_json())

# convert the object into a dict
api_users_user_id_mfa_verifications_post200_response_dict = api_users_user_id_mfa_verifications_post200_response_instance.to_dict()
# create an instance of ApiUsersUserIdMfaVerificationsPost200Response from a dict
api_users_user_id_mfa_verifications_post200_response_from_dict = ApiUsersUserIdMfaVerificationsPost200Response.from_dict(api_users_user_id_mfa_verifications_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


