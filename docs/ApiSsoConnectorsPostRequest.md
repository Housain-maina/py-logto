# ApiSsoConnectorsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | arbitrary | [optional] 
**domains** | **List[str]** |  | [optional] 
**branding** | [**ApiSsoConnectorsGet200ResponseInnerBranding**](ApiSsoConnectorsGet200ResponseInnerBranding.md) |  | [optional] 
**sync_profile** | **bool** |  | [optional] 
**provider_name** | **str** |  | 
**connector_name** | **str** |  | 

## Example

```python
from py_logto.models.api_sso_connectors_post_request import ApiSsoConnectorsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSsoConnectorsPostRequest from a JSON string
api_sso_connectors_post_request_instance = ApiSsoConnectorsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiSsoConnectorsPostRequest.to_json())

# convert the object into a dict
api_sso_connectors_post_request_dict = api_sso_connectors_post_request_instance.to_dict()
# create an instance of ApiSsoConnectorsPostRequest from a dict
api_sso_connectors_post_request_from_dict = ApiSsoConnectorsPostRequest.from_dict(api_sso_connectors_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


