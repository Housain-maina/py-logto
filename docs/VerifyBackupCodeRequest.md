# VerifyBackupCodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The backup code to verify. | 

## Example

```python
from py_logto.models.verify_backup_code_request import VerifyBackupCodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyBackupCodeRequest from a JSON string
verify_backup_code_request_instance = VerifyBackupCodeRequest.from_json(json)
# print the JSON string representation of the object
print(VerifyBackupCodeRequest.to_json())

# convert the object into a dict
verify_backup_code_request_dict = verify_backup_code_request_instance.to_dict()
# create an instance of VerifyBackupCodeRequest from a dict
verify_backup_code_request_from_dict = VerifyBackupCodeRequest.from_dict(verify_backup_code_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


