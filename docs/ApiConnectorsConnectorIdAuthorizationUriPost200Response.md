# ApiConnectorsConnectorIdAuthorizationUriPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect_to** | **str** |  | 
**redirect_uri** | **object** | The URI to navigate for authentication and authorization in the connected social identity provider. | [optional] 

## Example

```python
from py_logto.models.api_connectors_connector_id_authorization_uri_post200_response import ApiConnectorsConnectorIdAuthorizationUriPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiConnectorsConnectorIdAuthorizationUriPost200Response from a JSON string
api_connectors_connector_id_authorization_uri_post200_response_instance = ApiConnectorsConnectorIdAuthorizationUriPost200Response.from_json(json)
# print the JSON string representation of the object
print(ApiConnectorsConnectorIdAuthorizationUriPost200Response.to_json())

# convert the object into a dict
api_connectors_connector_id_authorization_uri_post200_response_dict = api_connectors_connector_id_authorization_uri_post200_response_instance.to_dict()
# create an instance of ApiConnectorsConnectorIdAuthorizationUriPost200Response from a dict
api_connectors_connector_id_authorization_uri_post200_response_from_dict = ApiConnectorsConnectorIdAuthorizationUriPost200Response.from_dict(api_connectors_connector_id_authorization_uri_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


