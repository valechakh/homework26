# Ex 1
# Գրել ֆունկցիա, որը,
# որպես արգումենտ կընդունի շրջանագծի շառավիղը (r) և սեկտորի անկյունը (alpha) ռադիաններով արտահայտված
# կհաշվի և կտպի համապատասխան շառավղով և անկյունով շրջանի մակերեսը,
# բանաձևը՝ S = (pi * r ** 2) * alpha / 360, բանաձևի մեջ alpha-ն արտահայտված է աստիճաններով


# import math

# def area(r, alpha):
#     alpha_convert = math.degrees(alpha)
#     S = (math.pi * r ** 2) * alpha_convert / 360
#     print(S)

# r = 3
# alpha_radians = math.radians(60)
# area(r, alpha_radians)
# O(1) complexity


# Ex 2
#  Գրել ֆունկցիա, որը․
#    - կստանա արգումենտ արաբական բնական թիվ (0-ից մեծ),
#    - կվերադրձնի այդ թիվը հռոմեական տեսքով,
#    հռոմեական թվերի համարժեքները՝ I-1, V-5, X-10, L-50, C-100, D-500, M-1000,
#    օրինակ՝ 15 -> XV,
#            72 -> LXXII,
#            9 -> IX

# def convert_to_roman(n):
#     roman_numbers = {
#         1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
#         40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
#         400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
#     }






# Ex 3
#  Գրել ֆունկցիա, որը․
#    - տրված բառերի list-ը կֆիլտրի այնպես, որ կթողի միայն ամենաերկար բառերը
#      (այսինքն՝ կգտնի ամենաերկար բառի երկարությունը և լիստում կթողնի միայն այդ երկարության բառերը)

# def longest_word(words):
#     max_length = 0
#     for i in words:
#         if len(i) > max_length:
#             max_length = len(i)
    
#     max_length_word = []
#     for j in words:
#         if len(j) == max_length:
#             max_length_word.append(j)
    
#     return max_length_word

# list1 = ["aba", "aa", "z", "ad", "vcd", "aba"]
# print(longest_word(list1))
# O(n) each of the loops