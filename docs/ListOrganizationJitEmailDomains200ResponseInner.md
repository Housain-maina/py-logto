# ListOrganizationJitEmailDomains200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**organization_id** | **str** |  | 
**email_domain** | **str** |  | 

## Example

```python
from py_logto.models.list_organization_jit_email_domains200_response_inner import ListOrganizationJitEmailDomains200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListOrganizationJitEmailDomains200ResponseInner from a JSON string
list_organization_jit_email_domains200_response_inner_instance = ListOrganizationJitEmailDomains200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListOrganizationJitEmailDomains200ResponseInner.to_json())

# convert the object into a dict
list_organization_jit_email_domains200_response_inner_dict = list_organization_jit_email_domains200_response_inner_instance.to_dict()
# create an instance of ListOrganizationJitEmailDomains200ResponseInner from a dict
list_organization_jit_email_domains200_response_inner_from_dict = ListOrganizationJitEmailDomains200ResponseInner.from_dict(list_organization_jit_email_domains200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


