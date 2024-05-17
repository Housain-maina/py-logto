# ApiApplicationsIdPatchRequestProtectedAppMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**origin** | **str** |  | [optional] 
**session_duration** | **float** |  | [optional] 
**page_rules** | [**List[ApiApplicationsGet200ResponseInnerProtectedAppMetadataPageRulesInner]**](ApiApplicationsGet200ResponseInnerProtectedAppMetadataPageRulesInner.md) |  | [optional] 

## Example

```python
from py_logto.models.api_applications_id_patch_request_protected_app_metadata import ApiApplicationsIdPatchRequestProtectedAppMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ApiApplicationsIdPatchRequestProtectedAppMetadata from a JSON string
api_applications_id_patch_request_protected_app_metadata_instance = ApiApplicationsIdPatchRequestProtectedAppMetadata.from_json(json)
# print the JSON string representation of the object
print(ApiApplicationsIdPatchRequestProtectedAppMetadata.to_json())

# convert the object into a dict
api_applications_id_patch_request_protected_app_metadata_dict = api_applications_id_patch_request_protected_app_metadata_instance.to_dict()
# create an instance of ApiApplicationsIdPatchRequestProtectedAppMetadata from a dict
api_applications_id_patch_request_protected_app_metadata_from_dict = ApiApplicationsIdPatchRequestProtectedAppMetadata.from_dict(api_applications_id_patch_request_protected_app_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


