# ApiSsoConnectorsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**provider_name** | **str** |  | 
**connector_name** | **str** |  | 
**config** | **object** | arbitrary | 
**domains** | **List[str]** |  | 
**branding** | [**ApiSsoConnectorsGet200ResponseInnerBranding**](ApiSsoConnectorsGet200ResponseInnerBranding.md) |  | 
**sync_profile** | **bool** |  | 
**created_at** | **float** |  | 
**name** | **str** |  | 
**provider_type** | **str** |  | 
**provider_logo** | **str** |  | 
**provider_logo_dark** | **str** |  | 
**provider_config** | **Dict[str, object]** |  | [optional] 

## Example

```python
from py_logto.models.api_sso_connectors_get200_response_inner import ApiSsoConnectorsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSsoConnectorsGet200ResponseInner from a JSON string
api_sso_connectors_get200_response_inner_instance = ApiSsoConnectorsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ApiSsoConnectorsGet200ResponseInner.to_json())

# convert the object into a dict
api_sso_connectors_get200_response_inner_dict = api_sso_connectors_get200_response_inner_instance.to_dict()
# create an instance of ApiSsoConnectorsGet200ResponseInner from a dict
api_sso_connectors_get200_response_inner_from_dict = ApiSsoConnectorsGet200ResponseInner.from_dict(api_sso_connectors_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


