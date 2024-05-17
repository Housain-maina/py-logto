# ApiOrganizationRolesIdScopesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_scope_ids** | **List[str]** | An array of organization scope IDs to be assigned. Existed scope IDs assignments will be ignored. | 

## Example

```python
from py_logto.models.api_organization_roles_id_scopes_post_request import ApiOrganizationRolesIdScopesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOrganizationRolesIdScopesPostRequest from a JSON string
api_organization_roles_id_scopes_post_request_instance = ApiOrganizationRolesIdScopesPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiOrganizationRolesIdScopesPostRequest.to_json())

# convert the object into a dict
api_organization_roles_id_scopes_post_request_dict = api_organization_roles_id_scopes_post_request_instance.to_dict()
# create an instance of ApiOrganizationRolesIdScopesPostRequest from a dict
api_organization_roles_id_scopes_post_request_from_dict = ApiOrganizationRolesIdScopesPostRequest.from_dict(api_organization_roles_id_scopes_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


