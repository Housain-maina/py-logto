# CreateResourceScopeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the scope. It should be unique for the resource. | 
**description** | **str** |  | [optional] 

## Example

```python
from py_logto.models.create_resource_scope_request import CreateResourceScopeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateResourceScopeRequest from a JSON string
create_resource_scope_request_instance = CreateResourceScopeRequest.from_json(json)
# print the JSON string representation of the object
print(CreateResourceScopeRequest.to_json())

# convert the object into a dict
create_resource_scope_request_dict = create_resource_scope_request_instance.to_dict()
# create an instance of CreateResourceScopeRequest from a dict
create_resource_scope_request_from_dict = CreateResourceScopeRequest.from_dict(create_resource_scope_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


