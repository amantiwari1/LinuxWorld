from boltiot import Sms

SID = "AC1e6ceaae1d533c27ae4eb1e2577a6e3b"

AUTH = "ac5c78ad809c724b3409715917dfbd4d"

FROM = "(863) 532-4946"

TO = "+919116623976"

sms = Sms(SID, AUTH, TO, FROM)

sms.send_sms("""" @@ suhhani pagal hai @@ """)