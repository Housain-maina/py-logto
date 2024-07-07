# UpdateAdminConsoleConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sign_in_experience_customized** | **bool** |  | [optional] 
**organization_created** | **bool** |  | [optional] 
**development_tenant_migration_notification** | [**GetAdminConsoleConfig200ResponseDevelopmentTenantMigrationNotification**](GetAdminConsoleConfig200ResponseDevelopmentTenantMigrationNotification.md) |  | [optional] 
**checked_charge_notification** | [**GetAdminConsoleConfig200ResponseCheckedChargeNotification**](GetAdminConsoleConfig200ResponseCheckedChargeNotification.md) |  | [optional] 

## Example

```python
from py_logto.models.update_admin_console_config_request import UpdateAdminConsoleConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminConsoleConfigRequest from a JSON string
update_admin_console_config_request_instance = UpdateAdminConsoleConfigRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminConsoleConfigRequest.to_json())

# convert the object into a dict
update_admin_console_config_request_dict = update_admin_console_config_request_instance.to_dict()
# create an instance of UpdateAdminConsoleConfigRequest from a dict
update_admin_console_config_request_from_dict = UpdateAdminConsoleConfigRequest.from_dict(update_admin_console_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


