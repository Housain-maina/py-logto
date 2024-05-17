# ApiOrganizationsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**created_at** | **float** |  | 
**users_count** | **float** |  | [optional] 
**featured_users** | [**List[ApiRolesGet200ResponseInnerFeaturedUsersInner]**](ApiRolesGet200ResponseInnerFeaturedUsersInner.md) |  | [optional] 

## Example

```python
from py_logto.models.api_organizations_get200_response_inner import ApiOrganizationsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOrganizationsGet200ResponseInner from a JSON string
api_organizations_get200_response_inner_instance = ApiOrganizationsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ApiOrganizationsGet200ResponseInner.to_json())

# convert the object into a dict
api_organizations_get200_response_inner_dict = api_organizations_get200_response_inner_instance.to_dict()
# create an instance of ApiOrganizationsGet200ResponseInner from a dict
api_organizations_get200_response_inner_from_dict = ApiOrganizationsGet200ResponseInner.from_dict(api_organizations_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


