# CreateUserIdentityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_id** | **str** | The Logto connector ID. | 
**connector_data** | **Dict[str, object]** | A json object constructed from the url query params returned by the social platform. Typically it contains &#x60;code&#x60;, &#x60;state&#x60; and &#x60;redirectUri&#x60; fields. | 

## Example

```python
from py_logto.models.create_user_identity_request import CreateUserIdentityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserIdentityRequest from a JSON string
create_user_identity_request_instance = CreateUserIdentityRequest.from_json(json)
# print the JSON string representation of the object
print(CreateUserIdentityRequest.to_json())

# convert the object into a dict
create_user_identity_request_dict = create_user_identity_request_instance.to_dict()
# create an instance of CreateUserIdentityRequest from a dict
create_user_identity_request_from_dict = CreateUserIdentityRequest.from_dict(create_user_identity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


