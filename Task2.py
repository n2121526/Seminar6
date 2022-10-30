#Задача 2. Напишите программу вычисления арифметического выражения заданного строкой. 
result = []
i = 0 

def calculation(sign, x, y):
        if sign == "+":
            return x + y
        elif sign == "-":
            return x - y
        elif sign == "/":
            return x / y
        elif sign == "*":
            return x * y


def difficult_calculation(symbol,beg = 0,finish = len(result),a = 0): 
    global result, i
    res_i = result[beg:finish].index(symbol) + a
    res = calculation(symbol, result[res_i-1], result[res_i+1]) 
    result.pop(res_i+1)  
    result.pop(res_i) 
    result.pop(res_i-1)                        
    result.insert(res_i-1,res) 
    i += 2 

str_i = input("Введите арифметическое выражение: ").strip()
num = ''
for ch in str_i:
    if ch.isdigit():
        num+=ch
    else: 
        if len(num)>0 and num.isdigit(): result.append(int(num))
        result.append(ch)
        num = ''

if len(num)>0 and num.isdigit(): result.append(int(num))        
result = list(filter((lambda el : el!= " " ),result))
  
while len(result) > 1:
    i = 0 
    while "(" in result: 
        r_index = (len(result) -1) - list(reversed(result)).index("(")
        try:
            ind = result.index(")")
        except:
            print("Выражение введено неверно")  
        result.pop(r_index)  
        result.pop(ind-1) 
       
    i = 0
    while "/" in result[r_index:ind-1-i]: 
            difficult_calculation("/",r_index, ind-1-i,r_index)
    while "*" in result[r_index:ind-1-i]:
            difficult_calculation("*",r_index, ind-1-i,r_index)    
    while "+" in result[r_index:ind-1-i]:
            difficult_calculation("+",r_index, ind-1-i,r_index)  
    while "-" in result[r_index:ind-1-i]:
            difficult_calculation("-",r_index, ind-1-i,r_index)    
    while "/" in result:
        difficult_calculation("/",0,len(result),0)
    while "*" in result:
        difficult_calculation("*",0,len(result),0)    
    while "+" in result:
        difficult_calculation("+",0,len(result),0)  
    while "-" in result:
        difficult_calculation("-",0,len(result),0)     
    
print(f" ==> {result[0]}")

