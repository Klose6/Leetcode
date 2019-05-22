"""
468 valid ip address
"""

def isValidIP(IP):
  def isIPv4(s):
    try: # check the str is a valid number
      return str(int(s)) == s and 0 <= int(s) <= 255
    except:
      return False
  def isIpv6(s):
    if len(s) > 4: return False
    try:
      return int(s, 16) >= 0 and s[0] != "-"
    except:
      return False
  if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):
    return "IPv4"
  elif IP.count(":") == 7 and all(isIpv6(i) for i in IP.split(":")):
    return "IPv6"
  return "Neither"

print(isValidIP("255.12.255.23"))