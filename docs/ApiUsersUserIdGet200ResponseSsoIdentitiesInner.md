# ApiUsersUserIdGet200ResponseSsoIdentitiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**issuer** | **str** |  | 
**identity_id** | **str** |  | 
**detail** | **object** | arbitrary | 
**created_at** | **float** |  | 
**sso_connector_id** | **str** |  | 

## Example

```python
from py_logto.models.api_users_user_id_get200_response_sso_identities_inner import ApiUsersUserIdGet200ResponseSsoIdentitiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiUsersUserIdGet200ResponseSsoIdentitiesInner from a JSON string
api_users_user_id_get200_response_sso_identities_inner_instance = ApiUsersUserIdGet200ResponseSsoIdentitiesInner.from_json(json)
# print the JSON string representation of the object
print(ApiUsersUserIdGet200ResponseSsoIdentitiesInner.to_json())

# convert the object into a dict
api_users_user_id_get200_response_sso_identities_inner_dict = api_users_user_id_get200_response_sso_identities_inner_instance.to_dict()
# create an instance of ApiUsersUserIdGet200ResponseSsoIdentitiesInner from a dict
api_users_user_id_get200_response_sso_identities_inner_from_dict = ApiUsersUserIdGet200ResponseSsoIdentitiesInner.from_dict(api_users_user_id_get200_response_sso_identities_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


