# ListApplicationRoles200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**type** | **str** |  | 
**is_default** | **bool** |  | 

## Example

```python
from py_logto.models.list_application_roles200_response_inner import ListApplicationRoles200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListApplicationRoles200ResponseInner from a JSON string
list_application_roles200_response_inner_instance = ListApplicationRoles200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListApplicationRoles200ResponseInner.to_json())

# convert the object into a dict
list_application_roles200_response_inner_dict = list_application_roles200_response_inner_instance.to_dict()
# create an instance of ListApplicationRoles200ResponseInner from a dict
list_application_roles200_response_inner_from_dict = ListApplicationRoles200ResponseInner.from_dict(list_application_roles200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


