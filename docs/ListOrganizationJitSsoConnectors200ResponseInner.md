# ListOrganizationJitSsoConnectors200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**id** | **str** |  | 
**provider_name** | **str** |  | 
**connector_name** | **str** |  | 
**config** | **object** | arbitrary | 
**domains** | **List[str]** |  | 
**branding** | [**ListOrganizationJitSsoConnectors200ResponseInnerBranding**](ListOrganizationJitSsoConnectors200ResponseInnerBranding.md) |  | 
**sync_profile** | **bool** |  | 
**created_at** | **float** |  | 

## Example

```python
from py_logto.models.list_organization_jit_sso_connectors200_response_inner import ListOrganizationJitSsoConnectors200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListOrganizationJitSsoConnectors200ResponseInner from a JSON string
list_organization_jit_sso_connectors200_response_inner_instance = ListOrganizationJitSsoConnectors200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListOrganizationJitSsoConnectors200ResponseInner.to_json())

# convert the object into a dict
list_organization_jit_sso_connectors200_response_inner_dict = list_organization_jit_sso_connectors200_response_inner_instance.to_dict()
# create an instance of ListOrganizationJitSsoConnectors200ResponseInner from a dict
list_organization_jit_sso_connectors200_response_inner_from_dict = ListOrganizationJitSsoConnectors200ResponseInner.from_dict(list_organization_jit_sso_connectors200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


