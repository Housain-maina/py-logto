# GetAdminConsoleConfig200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sign_in_experience_customized** | **bool** |  | 
**organization_created** | **bool** |  | 
**development_tenant_migration_notification** | [**GetAdminConsoleConfig200ResponseDevelopmentTenantMigrationNotification**](GetAdminConsoleConfig200ResponseDevelopmentTenantMigrationNotification.md) |  | [optional] 
**checked_charge_notification** | [**GetAdminConsoleConfig200ResponseCheckedChargeNotification**](GetAdminConsoleConfig200ResponseCheckedChargeNotification.md) |  | [optional] 

## Example

```python
from py_logto.models.get_admin_console_config200_response import GetAdminConsoleConfig200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAdminConsoleConfig200Response from a JSON string
get_admin_console_config200_response_instance = GetAdminConsoleConfig200Response.from_json(json)
# print the JSON string representation of the object
print(GetAdminConsoleConfig200Response.to_json())

# convert the object into a dict
get_admin_console_config200_response_dict = get_admin_console_config200_response_instance.to_dict()
# create an instance of GetAdminConsoleConfig200Response from a dict
get_admin_console_config200_response_from_dict = GetAdminConsoleConfig200Response.from_dict(get_admin_console_config200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


