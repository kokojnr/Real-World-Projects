# OTP project in Python
from twilio.rest import Client
import random

accountSSID = "ACbcb1a96857b73c07e9573467c4c18039"
authToken = "88050ddd0b4a85f6169e741d7ecf434b"
myClient = Client(accountSSID,authToken)

generateOTP = random.randint(100,999)
message = "Dear user your OTP is :" +str(generateOTP)

OTP = myClient.messages.create(
    from_= "+13342491372",
    body= message,
    to = "Your registered mobile number."
)

print(OTP.sid)
print(message)
