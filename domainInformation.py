import whois

def getDomainInfo():
    domain=input("Enter your domain name :")
    information=whois.whois(domain)
    print("Registrar",information['registrar'])
    print("Updated date :",information['updated_date'])
    print("Creation date :",information['creation_date'])
    print("Expiry :",information['expiration_date'])
    print("Email :",information['emails'])




getDomainInfo()
