# ApiOrganizationInvitationsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inviter_id** | **object** | The ID of the user who is inviting the user to join the organization. | [optional] 
**invitee** | **object** | The email address of the user to invite to join the organization. | [optional] 
**organization_id** | **object** | The ID of the organization to invite the user to join. | [optional] 
**expires_at** | **object** | The epoch time in milliseconds when the invitation expires. | [optional] 
**organization_role_ids** | **object** | The IDs of the organization roles to assign to the user when they accept the invitation. | [optional] 
**message_payload** | **object** | The message payload for the \&quot;OrganizationInvitation\&quot; template to use when sending the invitation via email. If it is &#x60;false&#x60;, the invitation will not be sent via email. | [optional] 

## Example

```python
from py_logto.models.api_organization_invitations_post_request import ApiOrganizationInvitationsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOrganizationInvitationsPostRequest from a JSON string
api_organization_invitations_post_request_instance = ApiOrganizationInvitationsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiOrganizationInvitationsPostRequest.to_json())

# convert the object into a dict
api_organization_invitations_post_request_dict = api_organization_invitations_post_request_instance.to_dict()
# create an instance of ApiOrganizationInvitationsPostRequest from a dict
api_organization_invitations_post_request_from_dict = ApiOrganizationInvitationsPostRequest.from_dict(api_organization_invitations_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


