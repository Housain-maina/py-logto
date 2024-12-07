# GenerateBackupCodes200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_id** | **str** | The unique verification ID of the newly created BackupCode verification record. This ID is required when adding the backup codes to the user profile via the Profile API. | 
**codes** | **List[str]** | The generated backup codes. | 

## Example

```python
from py_logto.models.generate_backup_codes200_response import GenerateBackupCodes200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateBackupCodes200Response from a JSON string
generate_backup_codes200_response_instance = GenerateBackupCodes200Response.from_json(json)
# print the JSON string representation of the object
print(GenerateBackupCodes200Response.to_json())

# convert the object into a dict
generate_backup_codes200_response_dict = generate_backup_codes200_response_instance.to_dict()
# create an instance of GenerateBackupCodes200Response from a dict
generate_backup_codes200_response_from_dict = GenerateBackupCodes200Response.from_dict(generate_backup_codes200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


