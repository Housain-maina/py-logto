# UpdateAccountCenterSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enable or disable the account API. | [optional] 
**fields** | [**UpdateAccountCenterSettingsRequestFields**](UpdateAccountCenterSettingsRequestFields.md) |  | [optional] 

## Example

```python
from py_logto.models.update_account_center_settings_request import UpdateAccountCenterSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAccountCenterSettingsRequest from a JSON string
update_account_center_settings_request_instance = UpdateAccountCenterSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAccountCenterSettingsRequest.to_json())

# convert the object into a dict
update_account_center_settings_request_dict = update_account_center_settings_request_instance.to_dict()
# create an instance of UpdateAccountCenterSettingsRequest from a dict
update_account_center_settings_request_from_dict = UpdateAccountCenterSettingsRequest.from_dict(update_account_center_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


