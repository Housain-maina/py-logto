# ReplaceOrganizationJitSsoConnectorsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sso_connector_ids** | **List[str]** | An array of SSO connector IDs to replace existing SSO connectors. | 

## Example

```python
from py_logto.models.replace_organization_jit_sso_connectors_request import ReplaceOrganizationJitSsoConnectorsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceOrganizationJitSsoConnectorsRequest from a JSON string
replace_organization_jit_sso_connectors_request_instance = ReplaceOrganizationJitSsoConnectorsRequest.from_json(json)
# print the JSON string representation of the object
print(ReplaceOrganizationJitSsoConnectorsRequest.to_json())

# convert the object into a dict
replace_organization_jit_sso_connectors_request_dict = replace_organization_jit_sso_connectors_request_instance.to_dict()
# create an instance of ReplaceOrganizationJitSsoConnectorsRequest from a dict
replace_organization_jit_sso_connectors_request_from_dict = ReplaceOrganizationJitSsoConnectorsRequest.from_dict(replace_organization_jit_sso_connectors_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


