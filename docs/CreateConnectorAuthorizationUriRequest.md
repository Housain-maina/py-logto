# CreateConnectorAuthorizationUriRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | A random string generated on the client side to prevent CSRF (Cross-Site Request Forgery) attacks. | 
**redirect_uri** | **str** | The URI to navigate back to after the user is authenticated by the connected social identity provider and has granted access to the connector. | 

## Example

```python
from py_logto.models.create_connector_authorization_uri_request import CreateConnectorAuthorizationUriRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConnectorAuthorizationUriRequest from a JSON string
create_connector_authorization_uri_request_instance = CreateConnectorAuthorizationUriRequest.from_json(json)
# print the JSON string representation of the object
print(CreateConnectorAuthorizationUriRequest.to_json())

# convert the object into a dict
create_connector_authorization_uri_request_dict = create_connector_authorization_uri_request_instance.to_dict()
# create an instance of CreateConnectorAuthorizationUriRequest from a dict
create_connector_authorization_uri_request_from_dict = CreateConnectorAuthorizationUriRequest.from_dict(create_connector_authorization_uri_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


