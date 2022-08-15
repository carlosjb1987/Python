import datetime

x = datetime.datetime.now()
xh=int(x.strftime("%H"))

if xh > 19 :
    print ("Son más de las 19")
else:
    y= 19 - xh
    print ("Te faltan ", y, " horas para terminar")

