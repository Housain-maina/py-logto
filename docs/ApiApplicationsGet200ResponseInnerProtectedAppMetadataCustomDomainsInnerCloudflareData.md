# ApiApplicationsGet200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**status** | **str** |  | 
**ssl** | [**ApiApplicationsGet200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareDataSsl**](ApiApplicationsGet200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareDataSsl.md) |  | 
**verification_errors** | **List[str]** |  | [optional] 

## Example

```python
from py_logto.models.api_applications_get200_response_inner_protected_app_metadata_custom_domains_inner_cloudflare_data import ApiApplicationsGet200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiApplicationsGet200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareData from a JSON string
api_applications_get200_response_inner_protected_app_metadata_custom_domains_inner_cloudflare_data_instance = ApiApplicationsGet200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareData.from_json(json)
# print the JSON string representation of the object
print(ApiApplicationsGet200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareData.to_json())

# convert the object into a dict
api_applications_get200_response_inner_protected_app_metadata_custom_domains_inner_cloudflare_data_dict = api_applications_get200_response_inner_protected_app_metadata_custom_domains_inner_cloudflare_data_instance.to_dict()
# create an instance of ApiApplicationsGet200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareData from a dict
api_applications_get200_response_inner_protected_app_metadata_custom_domains_inner_cloudflare_data_from_dict = ApiApplicationsGet200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareData.from_dict(api_applications_get200_response_inner_protected_app_metadata_custom_domains_inner_cloudflare_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


