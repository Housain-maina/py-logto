# CreateOrganizationRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 
**name** | **str** | The name of the organization role. It must be unique within the organization template. | 
**description** | **str** | The description of the organization role. | [optional] 
**type** | **str** |  | [optional] 
**organization_scope_ids** | **List[str]** | An array of organization scope IDs to be assigned to the organization role. | [default to []]
**resource_scope_ids** | **List[str]** | An array of resource scope IDs to be assigned to the organization role. | [default to []]

## Example

```python
from py_logto.models.create_organization_role_request import CreateOrganizationRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrganizationRoleRequest from a JSON string
create_organization_role_request_instance = CreateOrganizationRoleRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOrganizationRoleRequest.to_json())

# convert the object into a dict
create_organization_role_request_dict = create_organization_role_request_instance.to_dict()
# create an instance of CreateOrganizationRoleRequest from a dict
create_organization_role_request_from_dict = CreateOrganizationRoleRequest.from_dict(create_organization_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


