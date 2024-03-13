import datetime
import time

def formatIntegerPart(e: str):
    if len(e) <= 3:
        return e
    else:
        return (formatIntegerPart(e[0:len(e)-3]) + "," + e[len(e)-3:len(e)])

sec = time.time()
sec_scf = 56

sec_s = str(sec)
sec_coma = sec_s.index(".")

sec_int = sec_s[0:sec_coma]
sec_int = formatIntegerPart(sec_int)

sec_dec = sec_s[sec_coma + 1:sec_coma + 5]

d = datetime.datetime.now()

print(f'Seconds since January 1, 1970: {sec_int}.{sec_dec} or', "{:.2e}".format(sec),"in scientific notation") 
print(d.strftime("%b"), d.strftime("%m"), d.strftime("%Y"))


# ressources format lib datetime
# https://www.w3schools.com/python/python_datetime.asp
# https://www.tutorialspoint.com/display-scientific-notation-as-float-in-python
