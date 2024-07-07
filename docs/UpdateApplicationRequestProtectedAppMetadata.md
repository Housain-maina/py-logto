# UpdateApplicationRequestProtectedAppMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**origin** | **str** |  | [optional] 
**session_duration** | **float** |  | [optional] 
**page_rules** | [**List[ListApplications200ResponseInnerProtectedAppMetadataPageRulesInner]**](ListApplications200ResponseInnerProtectedAppMetadataPageRulesInner.md) |  | [optional] 

## Example

```python
from py_logto.models.update_application_request_protected_app_metadata import UpdateApplicationRequestProtectedAppMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateApplicationRequestProtectedAppMetadata from a JSON string
update_application_request_protected_app_metadata_instance = UpdateApplicationRequestProtectedAppMetadata.from_json(json)
# print the JSON string representation of the object
print(UpdateApplicationRequestProtectedAppMetadata.to_json())

# convert the object into a dict
update_application_request_protected_app_metadata_dict = update_application_request_protected_app_metadata_instance.to_dict()
# create an instance of UpdateApplicationRequestProtectedAppMetadata from a dict
update_application_request_protected_app_metadata_from_dict = UpdateApplicationRequestProtectedAppMetadata.from_dict(update_application_request_protected_app_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


