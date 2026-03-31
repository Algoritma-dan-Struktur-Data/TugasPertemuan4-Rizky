#Program Fizz Buzz
#Tampilkan angka 1-100
#Jika kelipatan 3, tampilkan "fizz"
#Jika kelipatan 5, tampilkan "buzz"
#Jika kelipatan keduanya, tampilkan keduanya "fizzbuzz"
#for dan percabangan

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)