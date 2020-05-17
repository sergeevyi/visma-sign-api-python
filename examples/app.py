import visma_sign
import requests
import json 

visma = visma_sign.ApiClient()

payload = {"document":{"name":"Java test"}}
documentUuid = visma.createDocument( json.dumps(payload) )
print( 'Created document '+documentUuid )

r = requests.get('https://sign.visma.net/empty.pdf', allow_redirects=True)
fileInfo = visma.addFile( documentUuid, r.content , 'empty.pdf')
print( 'Added file '+fileInfo )


invitation = [{ "email":"test@test.com",   "messages": { "send_invitation_email": True, "send_invitation_sms": False  }  }   ]
invitations  = visma.createInvitations(documentUuid, json.dumps(invitation) )
print( 'Created invitations ' +invitations.text )
invitation_uuid = json.loads(invitations.text)[0]['uuid']

fulfill = { 
        "returnUrl":"http://localhost:8080/fulfill-return/"+invitation_uuid, 
        "identifier":"010101-123N", 
        "authService":"tupas-nordea"
    }
fulfillUrl = visma.createFulfill(invitation_uuid, json.dumps(fulfill) )
print( 'Got fulfill url '+fulfillUrl.headers['Location'] )
