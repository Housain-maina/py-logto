# ApiUsersUserIdOrganizationsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**created_at** | **float** |  | 
**organization_roles** | [**List[ApiUsersUserIdOrganizationsGet200ResponseInnerOrganizationRolesInner]**](ApiUsersUserIdOrganizationsGet200ResponseInnerOrganizationRolesInner.md) |  | 

## Example

```python
from py_logto.models.api_users_user_id_organizations_get200_response_inner import ApiUsersUserIdOrganizationsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiUsersUserIdOrganizationsGet200ResponseInner from a JSON string
api_users_user_id_organizations_get200_response_inner_instance = ApiUsersUserIdOrganizationsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ApiUsersUserIdOrganizationsGet200ResponseInner.to_json())

# convert the object into a dict
api_users_user_id_organizations_get200_response_inner_dict = api_users_user_id_organizations_get200_response_inner_instance.to_dict()
# create an instance of ApiUsersUserIdOrganizationsGet200ResponseInner from a dict
api_users_user_id_organizations_get200_response_inner_from_dict = ApiUsersUserIdOrganizationsGet200ResponseInner.from_dict(api_users_user_id_organizations_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


