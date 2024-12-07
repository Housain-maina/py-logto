# UpdateAccountCenterSettingsRequestFields

The fields settings for the account API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**avatar** | **str** |  | [optional] 
**profile** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**social** | **str** |  | [optional] 
**custom_data** | **str** |  | [optional] 

## Example

```python
from py_logto.models.update_account_center_settings_request_fields import UpdateAccountCenterSettingsRequestFields

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAccountCenterSettingsRequestFields from a JSON string
update_account_center_settings_request_fields_instance = UpdateAccountCenterSettingsRequestFields.from_json(json)
# print the JSON string representation of the object
print(UpdateAccountCenterSettingsRequestFields.to_json())

# convert the object into a dict
update_account_center_settings_request_fields_dict = update_account_center_settings_request_fields_instance.to_dict()
# create an instance of UpdateAccountCenterSettingsRequestFields from a dict
update_account_center_settings_request_fields_from_dict = UpdateAccountCenterSettingsRequestFields.from_dict(update_account_center_settings_request_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


