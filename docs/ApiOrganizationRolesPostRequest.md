# ApiOrganizationRolesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the organization role. It must be unique within the organization template. | 
**description** | **str** | The description of the organization role. | [optional] 
**organization_scope_ids** | **List[str]** | An array of organization scope IDs to be assigned to the organization role. | [default to []]
**resource_scope_ids** | **object** | An array of resource scope IDs to be assigned to the organization role. | [optional] 

## Example

```python
from py_logto.models.api_organization_roles_post_request import ApiOrganizationRolesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOrganizationRolesPostRequest from a JSON string
api_organization_roles_post_request_instance = ApiOrganizationRolesPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiOrganizationRolesPostRequest.to_json())

# convert the object into a dict
api_organization_roles_post_request_dict = api_organization_roles_post_request_instance.to_dict()
# create an instance of ApiOrganizationRolesPostRequest from a dict
api_organization_roles_post_request_from_dict = ApiOrganizationRolesPostRequest.from_dict(api_organization_roles_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


