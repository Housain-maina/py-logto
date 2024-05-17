# ApiDomainsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**domain** | **str** |  | 
**status** | **str** |  | 
**error_message** | **str** |  | 
**dns_records** | [**List[ApiApplicationsGet200ResponseInnerProtectedAppMetadataCustomDomainsInnerDnsRecordsInner]**](ApiApplicationsGet200ResponseInnerProtectedAppMetadataCustomDomainsInnerDnsRecordsInner.md) |  | 

## Example

```python
from py_logto.models.api_domains_get200_response_inner import ApiDomainsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDomainsGet200ResponseInner from a JSON string
api_domains_get200_response_inner_instance = ApiDomainsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ApiDomainsGet200ResponseInner.to_json())

# convert the object into a dict
api_domains_get200_response_inner_dict = api_domains_get200_response_inner_instance.to_dict()
# create an instance of ApiDomainsGet200ResponseInner from a dict
api_domains_get200_response_inner_from_dict = ApiDomainsGet200ResponseInner.from_dict(api_domains_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


