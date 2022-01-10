import time
from time import sleep
import os
import uuid


def get_mac():
  mac_num = hex(uuid.getnode()).replace('0x', '').upper()
  mac = '-'.join(mac_num[i: i + 2] for i in range(0, 11, 2))
  return mac

print(uuid.getnode())
print(get_mac())
