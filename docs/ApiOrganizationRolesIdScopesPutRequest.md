# ApiOrganizationRolesIdScopesPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_scope_ids** | **List[str]** | An array of organization scope IDs to replace existing scopes. | 

## Example

```python
from py_logto.models.api_organization_roles_id_scopes_put_request import ApiOrganizationRolesIdScopesPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOrganizationRolesIdScopesPutRequest from a JSON string
api_organization_roles_id_scopes_put_request_instance = ApiOrganizationRolesIdScopesPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiOrganizationRolesIdScopesPutRequest.to_json())

# convert the object into a dict
api_organization_roles_id_scopes_put_request_dict = api_organization_roles_id_scopes_put_request_instance.to_dict()
# create an instance of ApiOrganizationRolesIdScopesPutRequest from a dict
api_organization_roles_id_scopes_put_request_from_dict = ApiOrganizationRolesIdScopesPutRequest.from_dict(api_organization_roles_id_scopes_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


