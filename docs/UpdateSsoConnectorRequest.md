# UpdateSsoConnectorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | arbitrary | [optional] 
**domains** | **List[str]** |  | [optional] 
**branding** | [**ListOrganizationJitSsoConnectors200ResponseInnerBranding**](ListOrganizationJitSsoConnectors200ResponseInnerBranding.md) |  | [optional] 
**sync_profile** | **bool** |  | [optional] 
**connector_name** | **str** |  | [optional] 

## Example

```python
from py_logto.models.update_sso_connector_request import UpdateSsoConnectorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSsoConnectorRequest from a JSON string
update_sso_connector_request_instance = UpdateSsoConnectorRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSsoConnectorRequest.to_json())

# convert the object into a dict
update_sso_connector_request_dict = update_sso_connector_request_instance.to_dict()
# create an instance of UpdateSsoConnectorRequest from a dict
update_sso_connector_request_from_dict = UpdateSsoConnectorRequest.from_dict(update_sso_connector_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


