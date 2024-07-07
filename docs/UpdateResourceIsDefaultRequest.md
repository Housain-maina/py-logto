# UpdateResourceIsDefaultRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_default** | **bool** | The updated value of the &#x60;isDefault&#x60; property. | 

## Example

```python
from py_logto.models.update_resource_is_default_request import UpdateResourceIsDefaultRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateResourceIsDefaultRequest from a JSON string
update_resource_is_default_request_instance = UpdateResourceIsDefaultRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateResourceIsDefaultRequest.to_json())

# convert the object into a dict
update_resource_is_default_request_dict = update_resource_is_default_request_instance.to_dict()
# create an instance of UpdateResourceIsDefaultRequest from a dict
update_resource_is_default_request_from_dict = UpdateResourceIsDefaultRequest.from_dict(update_resource_is_default_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


