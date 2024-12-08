def Validador(CPF):
    StringCPF = str(CPF)
    if len(StringCPF) != 11:
        print(f'CPF Invalido!')
        return
    ValidadorX = int(StringCPF[9])
    ValidadorY = int(StringCPF[10])
    
    Soma1 = 0
    Cont = 0

    for i in range(10,1,-1):
        NumbCPF = int(StringCPF[Cont])
        Soma1 += NumbCPF * i
        Cont += 1

    VerificadorX = 11-(Soma1%11)
    Soma2 = 0
    Cont = 0

    for i in range(11,1,-1):
        NumbCPF = int(StringCPF[Cont])
        Soma2 += NumbCPF * i
        Cont += 1

    VerificadorY = 11-(Soma2%11)

    if VerificadorX == ValidadorX and VerificadorY == ValidadorY:
        print(f'CPF Valido!')
    else:
        print('CPF Invalido!')    

CPF = int(input('Digite seu CPF: '))
Validador(CPF)