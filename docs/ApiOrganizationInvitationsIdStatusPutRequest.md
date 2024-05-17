# ApiOrganizationInvitationsIdStatusPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **object** | The status of the organization invitation. | [optional] 
**accepted_user_id** | **object** | The ID of the user who accepted the organization invitation. Required if the status is \&quot;Accepted\&quot;. | [optional] 

## Example

```python
from py_logto.models.api_organization_invitations_id_status_put_request import ApiOrganizationInvitationsIdStatusPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOrganizationInvitationsIdStatusPutRequest from a JSON string
api_organization_invitations_id_status_put_request_instance = ApiOrganizationInvitationsIdStatusPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiOrganizationInvitationsIdStatusPutRequest.to_json())

# convert the object into a dict
api_organization_invitations_id_status_put_request_dict = api_organization_invitations_id_status_put_request_instance.to_dict()
# create an instance of ApiOrganizationInvitationsIdStatusPutRequest from a dict
api_organization_invitations_id_status_put_request_from_dict = ApiOrganizationInvitationsIdStatusPutRequest.from_dict(api_organization_invitations_id_status_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


