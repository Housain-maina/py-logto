# ApiOrganizationRolesIdResourceScopesPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope_ids** | **object** | An array of resource scope IDs to replace existing scopes. | [optional] 

## Example

```python
from py_logto.models.api_organization_roles_id_resource_scopes_put_request import ApiOrganizationRolesIdResourceScopesPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOrganizationRolesIdResourceScopesPutRequest from a JSON string
api_organization_roles_id_resource_scopes_put_request_instance = ApiOrganizationRolesIdResourceScopesPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiOrganizationRolesIdResourceScopesPutRequest.to_json())

# convert the object into a dict
api_organization_roles_id_resource_scopes_put_request_dict = api_organization_roles_id_resource_scopes_put_request_instance.to_dict()
# create an instance of ApiOrganizationRolesIdResourceScopesPutRequest from a dict
api_organization_roles_id_resource_scopes_put_request_from_dict = ApiOrganizationRolesIdResourceScopesPutRequest.from_dict(api_organization_roles_id_resource_scopes_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


