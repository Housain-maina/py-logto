# ListApplications200ResponseInnerProtectedAppMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | 
**origin** | **str** |  | 
**session_duration** | **float** |  | 
**page_rules** | [**List[ListApplications200ResponseInnerProtectedAppMetadataPageRulesInner]**](ListApplications200ResponseInnerProtectedAppMetadataPageRulesInner.md) |  | 
**custom_domains** | [**List[ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInner]**](ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInner.md) |  | [optional] 

## Example

```python
from py_logto.models.list_applications200_response_inner_protected_app_metadata import ListApplications200ResponseInnerProtectedAppMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ListApplications200ResponseInnerProtectedAppMetadata from a JSON string
list_applications200_response_inner_protected_app_metadata_instance = ListApplications200ResponseInnerProtectedAppMetadata.from_json(json)
# print the JSON string representation of the object
print(ListApplications200ResponseInnerProtectedAppMetadata.to_json())

# convert the object into a dict
list_applications200_response_inner_protected_app_metadata_dict = list_applications200_response_inner_protected_app_metadata_instance.to_dict()
# create an instance of ListApplications200ResponseInnerProtectedAppMetadata from a dict
list_applications200_response_inner_protected_app_metadata_from_dict = ListApplications200ResponseInnerProtectedAppMetadata.from_dict(list_applications200_response_inner_protected_app_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


