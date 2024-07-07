# ListSsoConnectors200ResponseInner


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
**name** | **str** |  | 
**provider_type** | **str** |  | 
**provider_logo** | **str** |  | 
**provider_logo_dark** | **str** |  | 
**provider_config** | **Dict[str, object]** |  | [optional] 

## Example

```python
from py_logto.models.list_sso_connectors200_response_inner import ListSsoConnectors200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListSsoConnectors200ResponseInner from a JSON string
list_sso_connectors200_response_inner_instance = ListSsoConnectors200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListSsoConnectors200ResponseInner.to_json())

# convert the object into a dict
list_sso_connectors200_response_inner_dict = list_sso_connectors200_response_inner_instance.to_dict()
# create an instance of ListSsoConnectors200ResponseInner from a dict
list_sso_connectors200_response_inner_from_dict = ListSsoConnectors200ResponseInner.from_dict(list_sso_connectors200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


