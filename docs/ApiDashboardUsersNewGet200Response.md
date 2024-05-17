# ApiDashboardUsersNewGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**today** | [**ApiDashboardUsersNewGet200ResponseToday**](ApiDashboardUsersNewGet200ResponseToday.md) |  | 
**last7_days** | [**ApiDashboardUsersNewGet200ResponseToday**](ApiDashboardUsersNewGet200ResponseToday.md) |  | 

## Example

```python
from py_logto.models.api_dashboard_users_new_get200_response import ApiDashboardUsersNewGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDashboardUsersNewGet200Response from a JSON string
api_dashboard_users_new_get200_response_instance = ApiDashboardUsersNewGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiDashboardUsersNewGet200Response.to_json())

# convert the object into a dict
api_dashboard_users_new_get200_response_dict = api_dashboard_users_new_get200_response_instance.to_dict()
# create an instance of ApiDashboardUsersNewGet200Response from a dict
api_dashboard_users_new_get200_response_from_dict = ApiDashboardUsersNewGet200Response.from_dict(api_dashboard_users_new_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


