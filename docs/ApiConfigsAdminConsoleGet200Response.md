# ApiConfigsAdminConsoleGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sign_in_experience_customized** | **bool** |  | 
**organization_created** | **bool** |  | 
**development_tenant_migration_notification** | [**ApiConfigsAdminConsoleGet200ResponseDevelopmentTenantMigrationNotification**](ApiConfigsAdminConsoleGet200ResponseDevelopmentTenantMigrationNotification.md) |  | [optional] 
**checked_charge_notification** | [**ApiConfigsAdminConsoleGet200ResponseCheckedChargeNotification**](ApiConfigsAdminConsoleGet200ResponseCheckedChargeNotification.md) |  | [optional] 

## Example

```python
from py_logto.models.api_configs_admin_console_get200_response import ApiConfigsAdminConsoleGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiConfigsAdminConsoleGet200Response from a JSON string
api_configs_admin_console_get200_response_instance = ApiConfigsAdminConsoleGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiConfigsAdminConsoleGet200Response.to_json())

# convert the object into a dict
api_configs_admin_console_get200_response_dict = api_configs_admin_console_get200_response_instance.to_dict()
# create an instance of ApiConfigsAdminConsoleGet200Response from a dict
api_configs_admin_console_get200_response_from_dict = ApiConfigsAdminConsoleGet200Response.from_dict(api_configs_admin_console_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


