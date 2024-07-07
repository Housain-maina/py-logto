# UpdateResourceScopeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The updated name of the scope. It should be unique for the resource. | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from py_logto.models.update_resource_scope_request import UpdateResourceScopeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateResourceScopeRequest from a JSON string
update_resource_scope_request_instance = UpdateResourceScopeRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateResourceScopeRequest.to_json())

# convert the object into a dict
update_resource_scope_request_dict = update_resource_scope_request_instance.to_dict()
# create an instance of UpdateResourceScopeRequest from a dict
update_resource_scope_request_from_dict = UpdateResourceScopeRequest.from_dict(update_resource_scope_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


