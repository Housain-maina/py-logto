# ApiOrganizationsIdUsersGet200ResponseInner


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
**organization_roles** | [**List[ApiUsersUserIdOrganizationsGet200ResponseInnerOrganizationRolesInner]**](ApiUsersUserIdOrganizationsGet200ResponseInnerOrganizationRolesInner.md) |  | 

## Example

```python
from py_logto.models.api_organizations_id_users_get200_response_inner import ApiOrganizationsIdUsersGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOrganizationsIdUsersGet200ResponseInner from a JSON string
api_organizations_id_users_get200_response_inner_instance = ApiOrganizationsIdUsersGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ApiOrganizationsIdUsersGet200ResponseInner.to_json())

# convert the object into a dict
api_organizations_id_users_get200_response_inner_dict = api_organizations_id_users_get200_response_inner_instance.to_dict()
# create an instance of ApiOrganizationsIdUsersGet200ResponseInner from a dict
api_organizations_id_users_get200_response_inner_from_dict = ApiOrganizationsIdUsersGet200ResponseInner.from_dict(api_organizations_id_users_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


