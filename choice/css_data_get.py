import sys
sys.path.insert(1,r'E:\quantTradeLeanner\QuantTrader\choice\EMQuantAPI_Python\python3')
from EmQuantAPI import *
import pandas as pd
import numpy as np
import datetime

# 登录
try:
  loginresult = c.start("ForceLogin=1")
  print(loginresult)
except:
  pass
data=c.csd("110033.SH,110034.SH,110038.SH","CLOSE","2021-05-22","2021-06-12","type=1,period=1,adjustflag=1,curtype=1,order=1,market=CNSESH")
print(data)
# 登出
try:
  loginresult = c.stop()
  print(loginresult)
except:
  pass