#A prgram to manipulate strings

samp_string = "This is a very important sring"

print("Length : ", len(samp_string))

for i in range(0, len(samp_string)-1, 2):
    print(samp_string[1] + samp_string[i+1])

# A -Z 65-90
#a - z 97 - 122
print()
print("A = ", ord("A"))
print("65 = ", chr(65))
                  
