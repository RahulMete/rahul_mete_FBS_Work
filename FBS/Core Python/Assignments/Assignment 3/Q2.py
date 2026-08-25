#Write a program to input any alphabet and check whether it is vowel or consonant.

alpha = input('enter a aplhabet')

if(alpha=='a' or alpha=='e' or alpha=="i" or alpha=="o" or alpha=="u"):
    print(f'{alpha} is vowel')
else:
    print(f'{alpha} is consonant')