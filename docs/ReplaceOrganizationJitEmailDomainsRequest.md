# ReplaceOrganizationJitEmailDomainsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_domains** | **List[str]** | An array of email domains to replace existing email domains. | 

## Example

```python
from py_logto.models.replace_organization_jit_email_domains_request import ReplaceOrganizationJitEmailDomainsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceOrganizationJitEmailDomainsRequest from a JSON string
replace_organization_jit_email_domains_request_instance = ReplaceOrganizationJitEmailDomainsRequest.from_json(json)
# print the JSON string representation of the object
print(ReplaceOrganizationJitEmailDomainsRequest.to_json())

# convert the object into a dict
replace_organization_jit_email_domains_request_dict = replace_organization_jit_email_domains_request_instance.to_dict()
# create an instance of ReplaceOrganizationJitEmailDomainsRequest from a dict
replace_organization_jit_email_domains_request_from_dict = ReplaceOrganizationJitEmailDomainsRequest.from_dict(replace_organization_jit_email_domains_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


