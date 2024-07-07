# CreateOrganizationJitRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_role_ids** | **List[str]** | The organization role IDs to add. | 

## Example

```python
from py_logto.models.create_organization_jit_role_request import CreateOrganizationJitRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrganizationJitRoleRequest from a JSON string
create_organization_jit_role_request_instance = CreateOrganizationJitRoleRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOrganizationJitRoleRequest.to_json())

# convert the object into a dict
create_organization_jit_role_request_dict = create_organization_jit_role_request_instance.to_dict()
# create an instance of CreateOrganizationJitRoleRequest from a dict
create_organization_jit_role_request_from_dict = CreateOrganizationJitRoleRequest.from_dict(create_organization_jit_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


