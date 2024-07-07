# ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | 
**status** | **str** |  | 
**error_message** | **str** |  | 
**dns_records** | [**List[ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInnerDnsRecordsInner]**](ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInnerDnsRecordsInner.md) |  | 
**cloudflare_data** | [**ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareData**](ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareData.md) |  | 

## Example

```python
from py_logto.models.list_applications200_response_inner_protected_app_metadata_custom_domains_inner import ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInner from a JSON string
list_applications200_response_inner_protected_app_metadata_custom_domains_inner_instance = ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInner.from_json(json)
# print the JSON string representation of the object
print(ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInner.to_json())

# convert the object into a dict
list_applications200_response_inner_protected_app_metadata_custom_domains_inner_dict = list_applications200_response_inner_protected_app_metadata_custom_domains_inner_instance.to_dict()
# create an instance of ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInner from a dict
list_applications200_response_inner_protected_app_metadata_custom_domains_inner_from_dict = ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInner.from_dict(list_applications200_response_inner_protected_app_metadata_custom_domains_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


