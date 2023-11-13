def DeliverToken(sidorigin,sidto,token):
	if sidorigin==msg.sender and sidto!= NULL and Effective(token)and TokenOwns(token):
        oid = TokenIndexToResource(token)
        oattributes=GetAttributes(oid)
        allowedactions = GetPermission(token)
        env=GetEnvironmentAttr ()
        sidtoattri= GetAttributes(sidto)
        if Decision(oattributes,sidtoattri,env,allowedactions)==True:
	        TransferFrom(sidorigin,sidto,token)
	        return True
	    else:
            return False
    else:
        return False
