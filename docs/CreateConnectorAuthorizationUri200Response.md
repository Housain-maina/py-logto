# CreateConnectorAuthorizationUri200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect_to** | **str** |  | 
**redirect_uri** | **object** | The URI to navigate for authentication and authorization in the connected social identity provider. | [optional] 

## Example

```python
from py_logto.models.create_connector_authorization_uri200_response import CreateConnectorAuthorizationUri200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConnectorAuthorizationUri200Response from a JSON string
create_connector_authorization_uri200_response_instance = CreateConnectorAuthorizationUri200Response.from_json(json)
# print the JSON string representation of the object
print(CreateConnectorAuthorizationUri200Response.to_json())

# convert the object into a dict
create_connector_authorization_uri200_response_dict = create_connector_authorization_uri200_response_instance.to_dict()
# create an instance of CreateConnectorAuthorizationUri200Response from a dict
create_connector_authorization_uri200_response_from_dict = CreateConnectorAuthorizationUri200Response.from_dict(create_connector_authorization_uri200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


