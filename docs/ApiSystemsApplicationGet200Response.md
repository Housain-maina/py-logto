# ApiSystemsApplicationGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protected_apps** | [**ApiSystemsApplicationGet200ResponseProtectedApps**](ApiSystemsApplicationGet200ResponseProtectedApps.md) |  | 

## Example

```python
from py_logto.models.api_systems_application_get200_response import ApiSystemsApplicationGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSystemsApplicationGet200Response from a JSON string
api_systems_application_get200_response_instance = ApiSystemsApplicationGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiSystemsApplicationGet200Response.to_json())

# convert the object into a dict
api_systems_application_get200_response_dict = api_systems_application_get200_response_instance.to_dict()
# create an instance of ApiSystemsApplicationGet200Response from a dict
api_systems_application_get200_response_from_dict = ApiSystemsApplicationGet200Response.from_dict(api_systems_application_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


