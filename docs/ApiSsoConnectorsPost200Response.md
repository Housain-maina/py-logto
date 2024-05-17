# ApiSsoConnectorsPost200Response


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

## Example

```python
from py_logto.models.api_sso_connectors_post200_response import ApiSsoConnectorsPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSsoConnectorsPost200Response from a JSON string
api_sso_connectors_post200_response_instance = ApiSsoConnectorsPost200Response.from_json(json)
# print the JSON string representation of the object
print(ApiSsoConnectorsPost200Response.to_json())

# convert the object into a dict
api_sso_connectors_post200_response_dict = api_sso_connectors_post200_response_instance.to_dict()
# create an instance of ApiSsoConnectorsPost200Response from a dict
api_sso_connectors_post200_response_from_dict = ApiSsoConnectorsPost200Response.from_dict(api_sso_connectors_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


