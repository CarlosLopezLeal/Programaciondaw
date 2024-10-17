'''Crea un programa que dada una fecha en formato (dd-mm-yyyy), nos devuelva cuántos
días han transcurrido desde el 1 de enero de ese mismo año (considera que puede
tratarse de un año bisiesto).'''
day,month,year= 19,2,2024
total_days=0

if month== 1:
    total_days+=19
elif month== 2:
    total_days+=31
elif month== 3:
    total_days+=59
elif month== 4:
    total_days+=90
elif month== 5:
    total_days+=120
elif month== 6:
    total_days+=151
elif month== 7:
    total_days+=181
elif month== 8:
    total_days+=212
elif month== 9:
    total_days+=243
elif month== 10:
    total_days+=273
elif month== 11:
    total_days+=304
elif month== 12:
    total_days+= 334

total_days += day

if((year%4== 0) and (not year%100==0) or (year%400==0)):
    total_days+=1
print(total_days)