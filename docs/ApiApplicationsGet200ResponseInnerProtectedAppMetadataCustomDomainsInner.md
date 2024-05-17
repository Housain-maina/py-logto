# ApiApplicationsGet200ResponseInnerProtectedAppMetadataCustomDomainsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | 
**status** | **str** |  | 
**error_message** | **str** |  | 
**dns_records** | [**List[ApiApplicationsGet200ResponseInnerProtectedAppMetadataCustomDomainsInnerDnsRecordsInner]**](ApiApplicationsGet200ResponseInnerProtectedAppMetadataCustomDomainsInnerDnsRecordsInner.md) |  | 
**cloudflare_data** | [**ApiApplicationsGet200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareData**](ApiApplicationsGet200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareData.md) |  | 

## Example

```python
from py_logto.models.api_applications_get200_response_inner_protected_app_metadata_custom_domains_inner import ApiApplicationsGet200ResponseInnerProtectedAppMetadataCustomDomainsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiApplicationsGet200ResponseInnerProtectedAppMetadataCustomDomainsInner from a JSON string
api_applications_get200_response_inner_protected_app_metadata_custom_domains_inner_instance = ApiApplicationsGet200ResponseInnerProtectedAppMetadataCustomDomainsInner.from_json(json)
# print the JSON string representation of the object
print(ApiApplicationsGet200ResponseInnerProtectedAppMetadataCustomDomainsInner.to_json())

# convert the object into a dict
api_applications_get200_response_inner_protected_app_metadata_custom_domains_inner_dict = api_applications_get200_response_inner_protected_app_metadata_custom_domains_inner_instance.to_dict()
# create an instance of ApiApplicationsGet200ResponseInnerProtectedAppMetadataCustomDomainsInner from a dict
api_applications_get200_response_inner_protected_app_metadata_custom_domains_inner_from_dict = ApiApplicationsGet200ResponseInnerProtectedAppMetadataCustomDomainsInner.from_dict(api_applications_get200_response_inner_protected_app_metadata_custom_domains_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


