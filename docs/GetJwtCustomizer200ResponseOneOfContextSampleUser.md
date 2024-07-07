# GetJwtCustomizer200ResponseOneOfContextSampleUser


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
**identities** | [**Dict[str, GetJwtCustomizer200ResponseOneOfContextSampleUserIdentitiesValue]**](GetJwtCustomizer200ResponseOneOfContextSampleUserIdentitiesValue.md) |  | [optional] 
**last_sign_in_at** | **float** |  | [optional] 
**created_at** | **float** |  | [optional] 
**updated_at** | **float** |  | [optional] 
**profile** | [**GetJwtCustomizer200ResponseOneOfContextSampleUserProfile**](GetJwtCustomizer200ResponseOneOfContextSampleUserProfile.md) |  | [optional] 
**application_id** | **str** |  | [optional] 
**is_suspended** | **bool** |  | [optional] 
**has_password** | **bool** |  | [optional] 
**sso_identities** | [**List[GetJwtCustomizer200ResponseOneOfContextSampleUserSsoIdentitiesInner]**](GetJwtCustomizer200ResponseOneOfContextSampleUserSsoIdentitiesInner.md) |  | [optional] 
**mfa_verification_factors** | **List[str]** |  | [optional] 
**roles** | [**List[GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInner]**](GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInner.md) |  | [optional] 
**organizations** | [**List[ListApplicationUserConsentScopes200ResponseOrganizationScopesInner]**](ListApplicationUserConsentScopes200ResponseOrganizationScopesInner.md) |  | [optional] 
**organization_roles** | [**List[GetJwtCustomizer200ResponseOneOfContextSampleUserOrganizationRolesInner]**](GetJwtCustomizer200ResponseOneOfContextSampleUserOrganizationRolesInner.md) |  | [optional] 

## Example

```python
from py_logto.models.get_jwt_customizer200_response_one_of_context_sample_user import GetJwtCustomizer200ResponseOneOfContextSampleUser

# TODO update the JSON string below
json = "{}"
# create an instance of GetJwtCustomizer200ResponseOneOfContextSampleUser from a JSON string
get_jwt_customizer200_response_one_of_context_sample_user_instance = GetJwtCustomizer200ResponseOneOfContextSampleUser.from_json(json)
# print the JSON string representation of the object
print(GetJwtCustomizer200ResponseOneOfContextSampleUser.to_json())

# convert the object into a dict
get_jwt_customizer200_response_one_of_context_sample_user_dict = get_jwt_customizer200_response_one_of_context_sample_user_instance.to_dict()
# create an instance of GetJwtCustomizer200ResponseOneOfContextSampleUser from a dict
get_jwt_customizer200_response_one_of_context_sample_user_from_dict = GetJwtCustomizer200ResponseOneOfContextSampleUser.from_dict(get_jwt_customizer200_response_one_of_context_sample_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


