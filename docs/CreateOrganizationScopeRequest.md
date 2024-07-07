# CreateOrganizationScopeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 
**name** | **str** | The name of the organization scope. It must be unique within the organization template. | 
**description** | **str** | The description of the organization scope. | [optional] 

## Example

```python
from py_logto.models.create_organization_scope_request import CreateOrganizationScopeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrganizationScopeRequest from a JSON string
create_organization_scope_request_instance = CreateOrganizationScopeRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOrganizationScopeRequest.to_json())

# convert the object into a dict
create_organization_scope_request_dict = create_organization_scope_request_instance.to_dict()
# create an instance of CreateOrganizationScopeRequest from a dict
create_organization_scope_request_from_dict = CreateOrganizationScopeRequest.from_dict(create_organization_scope_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


