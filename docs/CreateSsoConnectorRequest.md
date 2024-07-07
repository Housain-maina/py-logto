# CreateSsoConnectorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | arbitrary | [optional] 
**domains** | **List[str]** |  | [optional] 
**branding** | [**ListOrganizationJitSsoConnectors200ResponseInnerBranding**](ListOrganizationJitSsoConnectors200ResponseInnerBranding.md) |  | [optional] 
**sync_profile** | **bool** |  | [optional] 
**provider_name** | **str** |  | 
**connector_name** | **str** |  | 

## Example

```python
from py_logto.models.create_sso_connector_request import CreateSsoConnectorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSsoConnectorRequest from a JSON string
create_sso_connector_request_instance = CreateSsoConnectorRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSsoConnectorRequest.to_json())

# convert the object into a dict
create_sso_connector_request_dict = create_sso_connector_request_instance.to_dict()
# create an instance of CreateSsoConnectorRequest from a dict
create_sso_connector_request_from_dict = CreateSsoConnectorRequest.from_dict(create_sso_connector_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


