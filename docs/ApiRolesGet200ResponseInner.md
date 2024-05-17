# ApiRolesGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**type** | **str** |  | 
**users_count** | **float** |  | 
**featured_users** | [**List[ApiRolesGet200ResponseInnerFeaturedUsersInner]**](ApiRolesGet200ResponseInnerFeaturedUsersInner.md) |  | 
**applications_count** | **float** |  | 
**featured_applications** | [**List[ApiRolesGet200ResponseInnerFeaturedApplicationsInner]**](ApiRolesGet200ResponseInnerFeaturedApplicationsInner.md) |  | 

## Example

```python
from py_logto.models.api_roles_get200_response_inner import ApiRolesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiRolesGet200ResponseInner from a JSON string
api_roles_get200_response_inner_instance = ApiRolesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ApiRolesGet200ResponseInner.to_json())

# convert the object into a dict
api_roles_get200_response_inner_dict = api_roles_get200_response_inner_instance.to_dict()
# create an instance of ApiRolesGet200ResponseInner from a dict
api_roles_get200_response_inner_from_dict = ApiRolesGet200ResponseInner.from_dict(api_roles_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


