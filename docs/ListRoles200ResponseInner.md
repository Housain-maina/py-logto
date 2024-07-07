# ListRoles200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**type** | **str** |  | 
**is_default** | **bool** |  | 
**users_count** | **float** |  | 
**featured_users** | [**List[ListRoles200ResponseInnerFeaturedUsersInner]**](ListRoles200ResponseInnerFeaturedUsersInner.md) |  | 
**applications_count** | **float** |  | 
**featured_applications** | [**List[ListRoles200ResponseInnerFeaturedApplicationsInner]**](ListRoles200ResponseInnerFeaturedApplicationsInner.md) |  | 

## Example

```python
from py_logto.models.list_roles200_response_inner import ListRoles200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListRoles200ResponseInner from a JSON string
list_roles200_response_inner_instance = ListRoles200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListRoles200ResponseInner.to_json())

# convert the object into a dict
list_roles200_response_inner_dict = list_roles200_response_inner_instance.to_dict()
# create an instance of ListRoles200ResponseInner from a dict
list_roles200_response_inner_from_dict = ListRoles200ResponseInner.from_dict(list_roles200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


