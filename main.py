import math

def primo(n):
    cont = 0 # contador
    if(n<2):
        return False 
    if (n % 2 ==0):
        if(n==2):
            return True
        else:
            return False
    else:
        cont=3
        while(cont<=math.sqrt(n)):
            if(n % cont == 0):
                return True
            else:
                cont = cont + 2 
    if(math.sqrt(n) < cont):
        return True


def mdcEuclides(a , b):
    t=True
    aux = 0    
      # r = resultado do mod
    while(t):
        r = a % b
        a = b
        aux = b
        b = r 
        if (r == 0 ):
            t = False
    return(aux)


def mmc(a,b): 
    resultado = (a * b) /(mdcEuclides(a,b))
    return resultado

#lambda de n
def lambdN(p , q):
    resultado = mmc(p-1, q-1)
    return resultado


def validaChavePublica(e):
    if (e>1 and e<lambdN):
        if(mdcEuclides(e,lambdN) ==1):
            return True
        else:
            return False



    
def chavePrivada_D(lamN,e):
    primeiroQuadrado = 0
    a = lamN
    b = lamN
    c = e
    d = 1
    while (primeiroQuadrado != 1):
        primeiroQuadrado = (a - math.floor(a/c) * c) % lamN
        segundoQuadrado = (b - math.floor(a/c) * d) % lamN
        a = c
        b = d
        c = primeiroQuadrado
        d = segundoQuadrado
        #print ("a",a,"b",b,"c",c,"d",d)
        #print (segundoQuadrado)
    return segundoQuadrado
    


#print(mmc(5,11))


def main():
    p = int(input("Digite P:\n"))
    while(primo(p) == False):
        print("Numero precisa ser primo")
        p = int(input("Digite P:\n"))
        

    q = int(input("Digite Q:\n"))
    while(primo(q) == False):
        print("Numero precisa ser primo")
        q = int(input("Digite Q:\n"))

    lamN=lambdN(p,q) # valor do P e Q na expressao lambda de N
    #print("valor do nosso lambda de N : ",lamN)

    # validando chave publica E 
    e = int(input("Digite E:\n"))
    while(e>=lamN or e<1):
        e = int(input("Digite E:\n"))
    mdc = mdcEuclides(e,lamN)
    while(mdc!=1):
        e = int(input("O E escolhido nao eh CO-PRIMO da funcao lambda(N) Digite E:\n"))
<<<<<<< HEAD
        mdc = mdcEuclides(e,lambN)
    
    print (lambN)   
    
    primeiroQuadrado = 0
    a = lambN
    b = lambN
    c = e
    d = 1
    while (primeiroQuadrado != 1):
        print ("a",a,"b",b,"c",c,"d",d)
        primeiroQuadrado = (a - math.floor(a/c) * c) % lambN
        segundoQuadrado = (b - math.floor(a/c) * d) % lambN
        a = c
        b = d
        c = primeiroQuadrado
        d = segundoQuadrado
        print ("a",a,"b",b,"c",c,"d",d)
        print (segundoQuadrado)
    
     
=======
        mdc = mdcEuclides(e,lamN)

    #mdc = mdcEuclides(e,lamN)
    #print(mdc)
    
    

    chave_d = chavePrivada_D(lamN, e )
    return chave_d

    
>>>>>>> 3341d873a912aaa919811ce2735eb0203b59ad8f
    


main()





