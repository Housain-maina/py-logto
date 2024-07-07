# CreateOrganizationJitSsoConnectorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sso_connector_ids** | **List[str]** | The SSO connector IDs to add. | 

## Example

```python
from py_logto.models.create_organization_jit_sso_connector_request import CreateOrganizationJitSsoConnectorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrganizationJitSsoConnectorRequest from a JSON string
create_organization_jit_sso_connector_request_instance = CreateOrganizationJitSsoConnectorRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOrganizationJitSsoConnectorRequest.to_json())

# convert the object into a dict
create_organization_jit_sso_connector_request_dict = create_organization_jit_sso_connector_request_instance.to_dict()
# create an instance of CreateOrganizationJitSsoConnectorRequest from a dict
create_organization_jit_sso_connector_request_from_dict = CreateOrganizationJitSsoConnectorRequest.from_dict(create_organization_jit_sso_connector_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


