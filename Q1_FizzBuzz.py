from xml.etree.ElementTree import tostring


for num in range(1, 101):
    string = ''

    # ここから記述
    #15は3,5の両方の倍数のため先に記述
    
    if num % 15 == 0:       #15の倍数のとき 
        string = 'FizzBuzz' #'FizzBuzz'と出力
    
    elif num % 3 == 0:      #3の倍数のとき
        string = 'Fizz'     #'Fizz'と出力
    
    elif num % 5 == 0:      #5の倍数のとき
        string = 'Buzz'     #'Buzz'と出力
    
    else:                   #それ以外のとき
        string = str(num)   #numを出力

    # ここまで記述

    print(string)