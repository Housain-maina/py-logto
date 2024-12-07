# GetEnabledSsoConnectors200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_ids** | **List[str]** | The list of enabled SSO connectorIds. Returns an empty array if no enabled SSO connectors are found. | 

## Example

```python
from py_logto.models.get_enabled_sso_connectors200_response import GetEnabledSsoConnectors200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEnabledSsoConnectors200Response from a JSON string
get_enabled_sso_connectors200_response_instance = GetEnabledSsoConnectors200Response.from_json(json)
# print the JSON string representation of the object
print(GetEnabledSsoConnectors200Response.to_json())

# convert the object into a dict
get_enabled_sso_connectors200_response_dict = get_enabled_sso_connectors200_response_instance.to_dict()
# create an instance of GetEnabledSsoConnectors200Response from a dict
get_enabled_sso_connectors200_response_from_dict = GetEnabledSsoConnectors200Response.from_dict(get_enabled_sso_connectors200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


