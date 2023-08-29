'''
txt = '"/home/user/Disco1.dsk"'
x = txt.split("/")[-1].replace('"', '')
print(x)
'''

from datetime import datetime
curr_dt = datetime.now()
timestamp = int(round(curr_dt.timestamp()))
timestamp_bytes = timestamp.to_bytes(8, byteorder='big')

print("Timestamp en bytes:", timestamp_bytes)
