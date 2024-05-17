# ApiUsersUserIdGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**username** | **str** |  | 
**primary_email** | **str** |  | 
**primary_phone** | **str** |  | 
**name** | **str** |  | 
**avatar** | **str** |  | 
**custom_data** | **object** | arbitrary | 
**identities** | [**Dict[str, ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserIdentitiesValue]**](ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserIdentitiesValue.md) |  | 
**last_sign_in_at** | **float** |  | 
**created_at** | **float** |  | 
**updated_at** | **float** |  | 
**profile** | [**ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserProfile**](ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserProfile.md) |  | 
**application_id** | **str** |  | 
**is_suspended** | **bool** |  | 
**has_password** | **bool** |  | [optional] 
**sso_identities** | [**List[ApiUsersUserIdGet200ResponseSsoIdentitiesInner]**](ApiUsersUserIdGet200ResponseSsoIdentitiesInner.md) | List of SSO identities associated with the user. Only available when the &#x60;includeSsoIdentities&#x60; query parameter is provided with a truthy value. | [optional] 

## Example

```python
from py_logto.models.api_users_user_id_get200_response import ApiUsersUserIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiUsersUserIdGet200Response from a JSON string
api_users_user_id_get200_response_instance = ApiUsersUserIdGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiUsersUserIdGet200Response.to_json())

# convert the object into a dict
api_users_user_id_get200_response_dict = api_users_user_id_get200_response_instance.to_dict()
# create an instance of ApiUsersUserIdGet200Response from a dict
api_users_user_id_get200_response_from_dict = ApiUsersUserIdGet200Response.from_dict(api_users_user_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


