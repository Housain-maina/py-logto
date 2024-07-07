# ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**status** | **str** |  | 
**ssl** | [**ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareDataSsl**](ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareDataSsl.md) |  | 
**verification_errors** | **List[str]** |  | [optional] 

## Example

```python
from py_logto.models.list_applications200_response_inner_protected_app_metadata_custom_domains_inner_cloudflare_data import ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareData

# TODO update the JSON string below
json = "{}"
# create an instance of ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareData from a JSON string
list_applications200_response_inner_protected_app_metadata_custom_domains_inner_cloudflare_data_instance = ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareData.from_json(json)
# print the JSON string representation of the object
print(ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareData.to_json())

# convert the object into a dict
list_applications200_response_inner_protected_app_metadata_custom_domains_inner_cloudflare_data_dict = list_applications200_response_inner_protected_app_metadata_custom_domains_inner_cloudflare_data_instance.to_dict()
# create an instance of ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareData from a dict
list_applications200_response_inner_protected_app_metadata_custom_domains_inner_cloudflare_data_from_dict = ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareData.from_dict(list_applications200_response_inner_protected_app_metadata_custom_domains_inner_cloudflare_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


