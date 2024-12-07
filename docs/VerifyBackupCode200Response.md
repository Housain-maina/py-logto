# VerifyBackupCode200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_id** | **str** | The unique verification ID of the BackupCode verification record. | 

## Example

```python
from py_logto.models.verify_backup_code200_response import VerifyBackupCode200Response

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyBackupCode200Response from a JSON string
verify_backup_code200_response_instance = VerifyBackupCode200Response.from_json(json)
# print the JSON string representation of the object
print(VerifyBackupCode200Response.to_json())

# convert the object into a dict
verify_backup_code200_response_dict = verify_backup_code200_response_instance.to_dict()
# create an instance of VerifyBackupCode200Response from a dict
verify_backup_code200_response_from_dict = VerifyBackupCode200Response.from_dict(verify_backup_code200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


