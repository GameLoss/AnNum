from prettytable import PrettyTable

myTable = PrettyTable(["i", "xl", "xu", "xr", "Error"])
xl = 2.9
xu = 3.1
xr = 0
xra = 0
b = 0

# Problema de prueba: 2.718281828459045**(-x) - x

def fx(x):
    xf= float(((-0.874)*(x**2)) + (1.75*(x)) + 2.627)
    return xf

def xrr(xl, xu, b):

    xr0=0
    if(b==1):
        xr0=(xl+xu)/2
    elif(b==2):
        xr0=(-(fx(xu))*(xl-xu))/(fx(xl)-fx(xu))+xu
    else:
        print("Opcion no valida")
        exit

    return xr0

def ea(xra, xr):
    ea=abs((xr-xra)/xr) * 100
    return ea

b = int(input("1.-Metodo Biseccion\n2.-Metodo Posicion Falsa\n"))
xr = xrr(xl,xu,b)

if (fx(xl)*fx(xu)<0):
    j=0
    k=0
    i=0
    err=0
    myTable.add_row([i, xl, xu, xr, err])
    a=True
    while(a):
        
        xra = xr
        
        if(fx(xl)*fx(xr)<0):
            xu=xr
            k+=1
        elif(fx(xl)*fx(xr)>0):
            xl=xr
            j+=1
        elif(fx(xl)*fx(xr)==0):
            a=False

        xr=xrr(xl,xu, b)
        i+=1
        err=ea(xra, xr)
        if(err<0.5):
            a=False
        myTable.add_row([i, xl, xu, xr, err])
    print(myTable)
else:
    print("La raiz no se encuentra en el intervalo")