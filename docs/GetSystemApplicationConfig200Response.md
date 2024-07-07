# GetSystemApplicationConfig200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protected_apps** | [**GetSystemApplicationConfig200ResponseProtectedApps**](GetSystemApplicationConfig200ResponseProtectedApps.md) |  | 

## Example

```python
from py_logto.models.get_system_application_config200_response import GetSystemApplicationConfig200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSystemApplicationConfig200Response from a JSON string
get_system_application_config200_response_instance = GetSystemApplicationConfig200Response.from_json(json)
# print the JSON string representation of the object
print(GetSystemApplicationConfig200Response.to_json())

# convert the object into a dict
get_system_application_config200_response_dict = get_system_application_config200_response_instance.to_dict()
# create an instance of GetSystemApplicationConfig200Response from a dict
get_system_application_config200_response_from_dict = GetSystemApplicationConfig200Response.from_dict(get_system_application_config200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


