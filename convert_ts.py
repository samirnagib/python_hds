import time
import datetime
stamp = 1635735600000
s, ms = divmod(stamp,1000)
print('%s.%03d' % (time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(s)), ms))
print('{}.{:03d}'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(s)), ms))

saida = stamp / 1000.0

print(datetime.datetime.fromtimestamp(saida).strftime('%Y-%M'))