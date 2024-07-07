# UpdateApplicationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**oidc_client_metadata** | [**UpdateApplicationRequestOidcClientMetadata**](UpdateApplicationRequestOidcClientMetadata.md) |  | [optional] 
**custom_client_metadata** | [**ListApplications200ResponseInnerCustomClientMetadata**](ListApplications200ResponseInnerCustomClientMetadata.md) |  | [optional] 
**protected_app_metadata** | [**UpdateApplicationRequestProtectedAppMetadata**](UpdateApplicationRequestProtectedAppMetadata.md) |  | [optional] 
**is_admin** | **bool** | Whether the application has admin access. User can enable the admin access for Machine-to-Machine apps. | [optional] 

## Example

```python
from py_logto.models.update_application_request import UpdateApplicationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateApplicationRequest from a JSON string
update_application_request_instance = UpdateApplicationRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateApplicationRequest.to_json())

# convert the object into a dict
update_application_request_dict = update_application_request_instance.to_dict()
# create an instance of UpdateApplicationRequest from a dict
update_application_request_from_dict = UpdateApplicationRequest.from_dict(update_application_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


