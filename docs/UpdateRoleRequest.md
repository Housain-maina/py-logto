# UpdateRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the role. It should be unique within the tenant. | [optional] 
**description** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 

## Example

```python
from py_logto.models.update_role_request import UpdateRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRoleRequest from a JSON string
update_role_request_instance = UpdateRoleRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateRoleRequest.to_json())

# convert the object into a dict
update_role_request_dict = update_role_request_instance.to_dict()
# create an instance of UpdateRoleRequest from a dict
update_role_request_from_dict = UpdateRoleRequest.from_dict(update_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


