print("整数Kを入力して下さい。1 <= K <= 5")
K = input()
try:
    print("ACL"*int(K))
except ValueError as err:
    print("\"" + K + "\"" + " is not int")
except Exception as other:
    print("Something else broke:", other)