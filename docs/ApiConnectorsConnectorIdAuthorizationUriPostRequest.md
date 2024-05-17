# ApiConnectorsConnectorIdAuthorizationUriPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | A random string generated on the client side to prevent CSRF (Cross-Site Request Forgery) attacks. | 
**redirect_uri** | **str** | The URI to navigate back to after the user is authenticated by the connected social identity provider and has granted access to the connector. | 

## Example

```python
from py_logto.models.api_connectors_connector_id_authorization_uri_post_request import ApiConnectorsConnectorIdAuthorizationUriPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiConnectorsConnectorIdAuthorizationUriPostRequest from a JSON string
api_connectors_connector_id_authorization_uri_post_request_instance = ApiConnectorsConnectorIdAuthorizationUriPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiConnectorsConnectorIdAuthorizationUriPostRequest.to_json())

# convert the object into a dict
api_connectors_connector_id_authorization_uri_post_request_dict = api_connectors_connector_id_authorization_uri_post_request_instance.to_dict()
# create an instance of ApiConnectorsConnectorIdAuthorizationUriPostRequest from a dict
api_connectors_connector_id_authorization_uri_post_request_from_dict = ApiConnectorsConnectorIdAuthorizationUriPostRequest.from_dict(api_connectors_connector_id_authorization_uri_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


