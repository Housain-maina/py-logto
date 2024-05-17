# ApiUsersUserIdMfaVerificationsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **str** |  | 
**type** | **str** |  | 
**agent** | **str** |  | [optional] 
**remain_codes** | **float** |  | [optional] 

## Example

```python
from py_logto.models.api_users_user_id_mfa_verifications_get200_response_inner import ApiUsersUserIdMfaVerificationsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiUsersUserIdMfaVerificationsGet200ResponseInner from a JSON string
api_users_user_id_mfa_verifications_get200_response_inner_instance = ApiUsersUserIdMfaVerificationsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ApiUsersUserIdMfaVerificationsGet200ResponseInner.to_json())

# convert the object into a dict
api_users_user_id_mfa_verifications_get200_response_inner_dict = api_users_user_id_mfa_verifications_get200_response_inner_instance.to_dict()
# create an instance of ApiUsersUserIdMfaVerificationsGet200ResponseInner from a dict
api_users_user_id_mfa_verifications_get200_response_inner_from_dict = ApiUsersUserIdMfaVerificationsGet200ResponseInner.from_dict(api_users_user_id_mfa_verifications_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


