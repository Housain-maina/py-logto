# CreateOrganizationJitEmailDomainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_domain** | **str** | The email domain to add. | 

## Example

```python
from py_logto.models.create_organization_jit_email_domain_request import CreateOrganizationJitEmailDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrganizationJitEmailDomainRequest from a JSON string
create_organization_jit_email_domain_request_instance = CreateOrganizationJitEmailDomainRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOrganizationJitEmailDomainRequest.to_json())

# convert the object into a dict
create_organization_jit_email_domain_request_dict = create_organization_jit_email_domain_request_instance.to_dict()
# create an instance of CreateOrganizationJitEmailDomainRequest from a dict
create_organization_jit_email_domain_request_from_dict = CreateOrganizationJitEmailDomainRequest.from_dict(create_organization_jit_email_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


