# CreateRoleScopeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope_ids** | **List[str]** | An array of API resource scope IDs to be linked. | 

## Example

```python
from py_logto.models.create_role_scope_request import CreateRoleScopeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRoleScopeRequest from a JSON string
create_role_scope_request_instance = CreateRoleScopeRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRoleScopeRequest.to_json())

# convert the object into a dict
create_role_scope_request_dict = create_role_scope_request_instance.to_dict()
# create an instance of CreateRoleScopeRequest from a dict
create_role_scope_request_from_dict = CreateRoleScopeRequest.from_dict(create_role_scope_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


