# ApiOrganizationRolesIdResourceScopesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope_ids** | **object** | An array of resource scope IDs to be assigned. Existed scope IDs assignments will be ignored. | [optional] 

## Example

```python
from py_logto.models.api_organization_roles_id_resource_scopes_post_request import ApiOrganizationRolesIdResourceScopesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOrganizationRolesIdResourceScopesPostRequest from a JSON string
api_organization_roles_id_resource_scopes_post_request_instance = ApiOrganizationRolesIdResourceScopesPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiOrganizationRolesIdResourceScopesPostRequest.to_json())

# convert the object into a dict
api_organization_roles_id_resource_scopes_post_request_dict = api_organization_roles_id_resource_scopes_post_request_instance.to_dict()
# create an instance of ApiOrganizationRolesIdResourceScopesPostRequest from a dict
api_organization_roles_id_resource_scopes_post_request_from_dict = ApiOrganizationRolesIdResourceScopesPostRequest.from_dict(api_organization_roles_id_resource_scopes_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


