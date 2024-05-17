# ApiSsoConnectorProvidersGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_name** | **str** |  | 
**provider_type** | **str** |  | 
**logo** | **str** |  | 
**logo_dark** | **str** |  | 
**description** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from py_logto.models.api_sso_connector_providers_get200_response_inner import ApiSsoConnectorProvidersGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSsoConnectorProvidersGet200ResponseInner from a JSON string
api_sso_connector_providers_get200_response_inner_instance = ApiSsoConnectorProvidersGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ApiSsoConnectorProvidersGet200ResponseInner.to_json())

# convert the object into a dict
api_sso_connector_providers_get200_response_inner_dict = api_sso_connector_providers_get200_response_inner_instance.to_dict()
# create an instance of ApiSsoConnectorProvidersGet200ResponseInner from a dict
api_sso_connector_providers_get200_response_inner_from_dict = ApiSsoConnectorProvidersGet200ResponseInner.from_dict(api_sso_connector_providers_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


