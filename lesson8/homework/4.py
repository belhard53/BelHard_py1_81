'''

Написать функцию, которая возвращает любое число в виде денежной величины 
с разделителями групп разрядов в качестве пробела и валютой в конце. 
Денежная величина всегда должна содержать количество копеек в виде дух 
знаков после точки, даже если исходное число целое. 
*Нельзя использовать форматную строку.
Например: 1234567 -> "1 234 567.00 руб."

с помощью try перехватить возможные ошибки.
'''

def num_format1(num, sep = " "):
    dec = str(int(num*100%100))
    num = int(num)
    res = ""    
    for s in str(num)[::-1]:
        res += s
        if len(res.replace(sep, ""))%3 == 0: 
            res += sep    
    
    
    return f"{res[::-1].strip()}.{dec.zfill(2)}"
    

def num_format2(num, sep = " "):
    dec = str(int(num*100))[-2:]
    num = int(num)
    num_str = sep.join([str(num)[::-1][i:i+3] for i in range(0,len(str(num)), 3)])[::-1]
    return f'{num_str}.{dec}'

def num_format3(num, sep = " "):
    return f"{num:_.2f}".replace("_", " ")



def num_format4(amount: float) -> str:
    try:
        if not isinstance(amount, (int, float)):
            raise ValueError("Переданное значение должно быть числом")
        
        currency, cents = "{:.2f}".format(amount).split(".")
        currency = " ".join(currency[::-1][i:i+3] for i in range(0, len(currency), 3))
        currency = currency[::-1]

        return "{}.{} руб.".format(currency, cents)
    except Exception as e:
        return "Ошибка: {}".format(e)


num_format = num_format4

print(num_format(12345678))
print(num_format(12345678.01))
print(num_format(12345678.1))
print(num_format(12_345_678.09))
print(num_format("12345678.09"))

    