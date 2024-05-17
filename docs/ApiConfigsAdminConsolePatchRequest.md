# ApiConfigsAdminConsolePatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sign_in_experience_customized** | **bool** |  | [optional] 
**organization_created** | **bool** |  | [optional] 
**development_tenant_migration_notification** | [**ApiConfigsAdminConsoleGet200ResponseDevelopmentTenantMigrationNotification**](ApiConfigsAdminConsoleGet200ResponseDevelopmentTenantMigrationNotification.md) |  | [optional] 
**checked_charge_notification** | [**ApiConfigsAdminConsoleGet200ResponseCheckedChargeNotification**](ApiConfigsAdminConsoleGet200ResponseCheckedChargeNotification.md) |  | [optional] 

## Example

```python
from py_logto.models.api_configs_admin_console_patch_request import ApiConfigsAdminConsolePatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiConfigsAdminConsolePatchRequest from a JSON string
api_configs_admin_console_patch_request_instance = ApiConfigsAdminConsolePatchRequest.from_json(json)
# print the JSON string representation of the object
print(ApiConfigsAdminConsolePatchRequest.to_json())

# convert the object into a dict
api_configs_admin_console_patch_request_dict = api_configs_admin_console_patch_request_instance.to_dict()
# create an instance of ApiConfigsAdminConsolePatchRequest from a dict
api_configs_admin_console_patch_request_from_dict = ApiConfigsAdminConsolePatchRequest.from_dict(api_configs_admin_console_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


