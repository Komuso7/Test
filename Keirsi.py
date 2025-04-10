from Const_Keirsi import *
def Stupid(AA):
    A = 0
    B = 0
    for i in AA:
        if i == "1":
            A += 1
        else:
            B += 1
    if A >= B:
        return '1'
    else:
        return '0'

def Keirsi(answers):
    counter = 1
    EI = []
    SN = []
    TF = []
    JP = []
    for i in answers:
        if counter == 1:
            EI += i
        elif counter == 2 or counter == 3:
            SN += i
        elif counter == 4 or counter == 5:
            TF += i
        else:
            JP += i
        counter += 1
        if counter == 8:
            counter = 1

    answer = Stupid(EI)
    answer += Stupid(SN)
    answer += Stupid(TF)
    answer += Stupid(JP)
    if answer == "0000":
        answer = INFP
    elif answer == "0001":
        answer = INFJ
    elif answer == "0010":
        answer = INTP
    elif answer == "0011":
        answer = INTJ
    elif answer == "0100":
        answer = ISFP
    elif answer == "0101":
        answer = ISFJ
    elif answer == "0110":
        answer = ISTP
    elif answer == "0111":
        answer = ISTJ
    elif answer == "1000":
        answer = ENFP
    elif answer == "1001":
        answer = ENFJ
    elif answer == "1010":
        answer = ENTP
    elif answer == "1011":
        answer = ENTJ
    elif answer == "1100":
        answer = ESFP
    elif answer == "1101":
        answer = ESFJ
    elif answer == "1110":
        answer = ESTP
    elif answer == "1111":
        answer = ESTJ
    return answer