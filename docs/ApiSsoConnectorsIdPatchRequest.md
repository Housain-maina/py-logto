# ApiSsoConnectorsIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | arbitrary | [optional] 
**domains** | **List[str]** |  | [optional] 
**branding** | [**ApiSsoConnectorsGet200ResponseInnerBranding**](ApiSsoConnectorsGet200ResponseInnerBranding.md) |  | [optional] 
**sync_profile** | **bool** |  | [optional] 
**connector_name** | **str** |  | [optional] 

## Example

```python
from py_logto.models.api_sso_connectors_id_patch_request import ApiSsoConnectorsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSsoConnectorsIdPatchRequest from a JSON string
api_sso_connectors_id_patch_request_instance = ApiSsoConnectorsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(ApiSsoConnectorsIdPatchRequest.to_json())

# convert the object into a dict
api_sso_connectors_id_patch_request_dict = api_sso_connectors_id_patch_request_instance.to_dict()
# create an instance of ApiSsoConnectorsIdPatchRequest from a dict
api_sso_connectors_id_patch_request_from_dict = ApiSsoConnectorsIdPatchRequest.from_dict(api_sso_connectors_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


