# ApiApplicationsGet200ResponseInnerProtectedAppMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | 
**origin** | **str** |  | 
**session_duration** | **float** |  | 
**page_rules** | [**List[ApiApplicationsGet200ResponseInnerProtectedAppMetadataPageRulesInner]**](ApiApplicationsGet200ResponseInnerProtectedAppMetadataPageRulesInner.md) |  | 
**custom_domains** | [**List[ApiApplicationsGet200ResponseInnerProtectedAppMetadataCustomDomainsInner]**](ApiApplicationsGet200ResponseInnerProtectedAppMetadataCustomDomainsInner.md) |  | [optional] 

## Example

```python
from py_logto.models.api_applications_get200_response_inner_protected_app_metadata import ApiApplicationsGet200ResponseInnerProtectedAppMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ApiApplicationsGet200ResponseInnerProtectedAppMetadata from a JSON string
api_applications_get200_response_inner_protected_app_metadata_instance = ApiApplicationsGet200ResponseInnerProtectedAppMetadata.from_json(json)
# print the JSON string representation of the object
print(ApiApplicationsGet200ResponseInnerProtectedAppMetadata.to_json())

# convert the object into a dict
api_applications_get200_response_inner_protected_app_metadata_dict = api_applications_get200_response_inner_protected_app_metadata_instance.to_dict()
# create an instance of ApiApplicationsGet200ResponseInnerProtectedAppMetadata from a dict
api_applications_get200_response_inner_protected_app_metadata_from_dict = ApiApplicationsGet200ResponseInnerProtectedAppMetadata.from_dict(api_applications_get200_response_inner_protected_app_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


