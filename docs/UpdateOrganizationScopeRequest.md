# UpdateOrganizationScopeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** | The updated name of the organization scope. It must be unique within the organization template. | [optional] 
**description** | **str** | The updated description of the organization scope. | [optional] 

## Example

```python
from py_logto.models.update_organization_scope_request import UpdateOrganizationScopeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrganizationScopeRequest from a JSON string
update_organization_scope_request_instance = UpdateOrganizationScopeRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateOrganizationScopeRequest.to_json())

# convert the object into a dict
update_organization_scope_request_dict = update_organization_scope_request_instance.to_dict()
# create an instance of UpdateOrganizationScopeRequest from a dict
update_organization_scope_request_from_dict = UpdateOrganizationScopeRequest.from_dict(update_organization_scope_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


