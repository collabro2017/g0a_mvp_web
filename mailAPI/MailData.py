def getData(option)

    with open('pkl/emailsDict.pkl','rb') as f:
        emailsDict = pickle.load(f)


    isNumber = True

    try:
        mailsLen = int(mailsLen)
    except ValueError :
        isNumber= False

    if not isNumber:
        mailsLen = len(emailsDict)
    else:
        if mailsLen>len(emailsDict):
            mailsLen = len(emailsDict)

    if(option == 'default'):
        return(emailsDict[:mailsLen])
    elif(option == 'content'):
        return emailsDict[:mailsLen]['email']['emailText']
    elif(option == "subject"):
        return emailsDict[:mailsLen]['email']['Subject']
    elif(option == "from"):
            return emailsDict[:mailsLen]['email']['From']
    elif(option == "id"):
        return emailsDict[:mailsLen]['id']