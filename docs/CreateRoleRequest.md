# CreateRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 
**name** | **str** | The name of the role. It should be unique within the tenant. | 
**description** | **str** |  | 
**type** | **str** | The type of the role. It cannot be changed after creation. | [optional] 
**is_default** | **bool** |  | [optional] 
**scope_ids** | **List[str]** | The initial API resource scopes assigned to the role. | [optional] 

## Example

```python
from py_logto.models.create_role_request import CreateRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRoleRequest from a JSON string
create_role_request_instance = CreateRoleRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRoleRequest.to_json())

# convert the object into a dict
create_role_request_dict = create_role_request_instance.to_dict()
# create an instance of CreateRoleRequest from a dict
create_role_request_from_dict = CreateRoleRequest.from_dict(create_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


