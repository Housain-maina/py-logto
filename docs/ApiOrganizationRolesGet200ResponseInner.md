# ApiOrganizationRolesGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**scopes** | [**List[ApiUsersUserIdOrganizationsGet200ResponseInnerOrganizationRolesInner]**](ApiUsersUserIdOrganizationsGet200ResponseInnerOrganizationRolesInner.md) |  | 

## Example

```python
from py_logto.models.api_organization_roles_get200_response_inner import ApiOrganizationRolesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOrganizationRolesGet200ResponseInner from a JSON string
api_organization_roles_get200_response_inner_instance = ApiOrganizationRolesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ApiOrganizationRolesGet200ResponseInner.to_json())

# convert the object into a dict
api_organization_roles_get200_response_inner_dict = api_organization_roles_get200_response_inner_instance.to_dict()
# create an instance of ApiOrganizationRolesGet200ResponseInner from a dict
api_organization_roles_get200_response_inner_from_dict = ApiOrganizationRolesGet200ResponseInner.from_dict(api_organization_roles_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


