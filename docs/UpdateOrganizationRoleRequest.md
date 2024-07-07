# UpdateOrganizationRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** | The updated name of the organization role. It must be unique within the organization template. | [optional] 
**description** | **str** | The updated description of the organization role. | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from py_logto.models.update_organization_role_request import UpdateOrganizationRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrganizationRoleRequest from a JSON string
update_organization_role_request_instance = UpdateOrganizationRoleRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateOrganizationRoleRequest.to_json())

# convert the object into a dict
update_organization_role_request_dict = update_organization_role_request_instance.to_dict()
# create an instance of UpdateOrganizationRoleRequest from a dict
update_organization_role_request_from_dict = UpdateOrganizationRoleRequest.from_dict(update_organization_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


