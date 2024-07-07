# ListSsoConnectorProviders200ResponseInner


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
from py_logto.models.list_sso_connector_providers200_response_inner import ListSsoConnectorProviders200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListSsoConnectorProviders200ResponseInner from a JSON string
list_sso_connector_providers200_response_inner_instance = ListSsoConnectorProviders200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListSsoConnectorProviders200ResponseInner.to_json())

# convert the object into a dict
list_sso_connector_providers200_response_inner_dict = list_sso_connector_providers200_response_inner_instance.to_dict()
# create an instance of ListSsoConnectorProviders200ResponseInner from a dict
list_sso_connector_providers200_response_inner_from_dict = ListSsoConnectorProviders200ResponseInner.from_dict(list_sso_connector_providers200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


