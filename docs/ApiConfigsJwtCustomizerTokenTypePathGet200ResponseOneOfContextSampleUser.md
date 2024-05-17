# ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**primary_email** | **str** |  | [optional] 
**primary_phone** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**avatar** | **str** |  | [optional] 
**custom_data** | **object** | arbitrary | [optional] 
**identities** | [**Dict[str, ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserIdentitiesValue]**](ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserIdentitiesValue.md) |  | [optional] 
**last_sign_in_at** | **float** |  | [optional] 
**created_at** | **float** |  | [optional] 
**updated_at** | **float** |  | [optional] 
**profile** | [**ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserProfile**](ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserProfile.md) |  | [optional] 
**application_id** | **str** |  | [optional] 
**is_suspended** | **bool** |  | [optional] 
**sso_identities** | [**List[ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserSsoIdentitiesInner]**](ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserSsoIdentitiesInner.md) |  | [optional] 
**mfa_verification_factors** | **List[str]** |  | [optional] 
**roles** | [**List[ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserRolesInner]**](ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserRolesInner.md) |  | [optional] 
**organizations** | [**List[ApiApplicationsApplicationIdUserConsentScopesGet200ResponseOrganizationScopesInner]**](ApiApplicationsApplicationIdUserConsentScopesGet200ResponseOrganizationScopesInner.md) |  | [optional] 
**organization_roles** | [**List[ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserOrganizationRolesInner]**](ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserOrganizationRolesInner.md) |  | [optional] 

## Example

```python
from py_logto.models.api_configs_jwt_customizer_token_type_path_get200_response_one_of_context_sample_user import ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUser

# TODO update the JSON string below
json = "{}"
# create an instance of ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUser from a JSON string
api_configs_jwt_customizer_token_type_path_get200_response_one_of_context_sample_user_instance = ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUser.from_json(json)
# print the JSON string representation of the object
print(ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUser.to_json())

# convert the object into a dict
api_configs_jwt_customizer_token_type_path_get200_response_one_of_context_sample_user_dict = api_configs_jwt_customizer_token_type_path_get200_response_one_of_context_sample_user_instance.to_dict()
# create an instance of ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUser from a dict
api_configs_jwt_customizer_token_type_path_get200_response_one_of_context_sample_user_from_dict = ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUser.from_dict(api_configs_jwt_customizer_token_type_path_get200_response_one_of_context_sample_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


