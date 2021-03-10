'''
This program converts numbers to words. For example '1' is converted to 'one'.
The current code can convert up to 9 digits in Metric form, i.e. tens of crores.
This can be extended to Imperial with additional code. The code for Metric and Imperial is same
up to 5 digits, i.e. tens of thousands.
This program was first written during Nineties, in a procedural language COBOL,
using Tables definition and Search command, for cheque printing of Financial Applications.
The original program ran into hundreds of lines, because of the nature of the Language.
Mapped the same logic here, to demonstrate how Python can perform the same functionality
with less code.
This code can be optimized further, but the objective here is to demonstrate the functionality.
For testing purposes, test data is embedded in the code. The program can be altered to read
the data from file.
The program first converts the variable length input into fixed length and string processing
starts from left to right.
The test data covers various scenarios as listed below
figs : 1  words :  one
figs : 12  words :  twelve
figs : 123  words :  one hundred and twenty three
figs : 1234  words :  one thousand two hundred and thirty four
figs : 12345  words :  twelve thousand three hundred and forty five
figs : 123456  words :  one lakh twenty three thousand four hundred and fifty six
figs : 1234567  words :  twelve lakhs thirty four thousand five hundred and sixty seven
figs : 12345678  words :  one crore twenty three lakhs forty five thousand six hundred and seventy eight
figs : 123456789  words :  twelve crores thirty four lakhs fifty six thousand seven hundred and eighty nine
figs : 10  words :  ten
figs : 100  words :  one hundred
figs : 1000  words :  one thousand
figs : 10000  words :  ten thousand
figs : 100000  words :  one lakh
figs : 1000000  words :  ten lakhs
figs : 10000000  words :  one crore
figs : 100000000  words :  ten crores
figs : 101  words :  one hundred and one
figs : 1001  words :  one thousand and one
figs : 10001  words :  ten thousand and one
figs : 100001  words :  one lakh and one
figs : 1000001  words :  ten lakhs and one
figs : 10000001  words :  one crore and one
figs : 19  words :  nineteen
figs : 99  words :  ninety nine
figs : 999  words :  nine hundred and ninety nine
figs : 999999999  words :  ninety nine crores ninety nine lakhs ninety nine thousand nine hundred and ninety nine
figs : 20  words :  twenty
figs : 220  words :  two hundred and twenty
figs : 2220  words :  two thousand two hundred and twenty
figs : 20220  words :  twenty thousand two hundred and twenty
figs : 220220  words :  two lakh twenty thousand two hundred and twenty
figs : 2022020  words :  twenty lakhs and twenty two thousand and twenty
figs : 22022020  words :  two crore and twenty lakhs and twenty two thousand and twenty
figs : 202202200  words :  twenty crores twenty two lakhs two thousand two hundred
'2020220221' Invalid input. Can accept up to 9 digits only for now
figs : 11  words :  eleven
figs : 111  words :  one hundred and eleven
figs : 1111  words :  one thousand one hundred and eleven
figs : 11111  words :  eleven thousand one hundred and eleven
figs : 111111  words :  one lakh eleven thousand one hundred and eleven
figs : 1111111  words :  eleven lakhs eleven thousand one hundred and eleven
figs : 11111111  words :  one crore eleven lakhs eleven thousand one hundred and eleven
figs : 111111111  words :  eleven crores eleven lakhs eleven thousand one hundred and eleven
'abcd' Invalid input. Only integers allowed
'999999999999' Invalid input. Can accept up to 9 digits only for now
'''

import io
input_file = open("figstowords_input.txt", "r")
output_file = open("figstowords_out.txt", "w")
test_data_1 = ('1','12','123','1234','12345','123456','1234567','12345678','123456789')
test_data_2 = ('10','100','1000','10000','100000','1000000','10000000','100000000')
test_data_3 = ('101','1001','10001','100001','1000001','10000001','19','99','999')
test_data_4 = ('999999999','20','220','2220','20220','220220','2022020','22022020','202202200','2020220221')
test_data_5 = ('11','111','1111','11111','111111','1111111','11111111','111111111')
test_data_6 = ('abcd','999999999999')
test_data = (test_data_1 + test_data_2 + test_data_3 + test_data_4 + test_data_5 + test_data_6)

unit_figs = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
unit_words = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
teens_figs = (10,11,12,13,14,15,16,17,18,19)
teens_words = ('ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen')
word_map_1 = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}
word_map_2 = {
        00 : "",
        10 : "ten",
        20 : "twenty",
        30 : "thirty",
        40 : "forty",
        50 : "fifty",
        60 : "sixty",
        70 : "seventy",
        80 : "eighty",
        90 : "ninety"
}
word_map_3 = {
    00: "",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

tens = ('ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety')
hundreds = ('hundred ')
thousands = ('thousand ')
lakh = ("lakh ")
lakhs = ('lakhs ')
crore = ('crore ')
crores = ('crores ')
million = ('million ')
billion = ('billion ')
# define return variables
word_string = " "
exp_code = " "

def check_user_input(input):
    try:
        # validate input for numeric
        val = int(input)
        valid_input = 'Y'
    except ValueError:
        valid_input = 'N'
    return valid_input

def figs_to_words_metric(input_number):
    input_number_fixed = input_number.zfill(9)
    word_string = " "
    crores_flag = "N"
    if int(input_number_fixed[0:2]) > 0:
        crores_word_string = crores_map(input_number_fixed[0:2])
        crores_flag = "Y"

    lakhs_flag = "N"
    if int(input_number_fixed[2:4]) > 0:
        lakhs_word_string = lakhs_map(input_number_fixed[2:4])
        lakhs_flag = "Y"

    thousands_flag = "N"
    if int(input_number_fixed[4:6]) > 0:
        thousands_word_string = thousands_map(input_number_fixed[4:6])
        thousands_flag = "Y"

    hundreds_flag = "N"
    if int(input_number_fixed[6:7]) > 0:
        hundreds_word_string = hundreds_map(input_number_fixed[6:7])
        hundreds_flag = "Y"

    tens_flag = "N"
    units_flag = "N"
    if int(input_number_fixed[7:]) > 0:
        tens_units = input_number_fixed[7:]
        if int(tens_units[0]) > 0:
           tens_word_string = tens_map(tens_units)
           tens_flag = "Y"
        else:
           units_word_string = units_map(tens_units)
           units_flag = "Y"

    if crores_flag == "Y":
        word_string += crores_word_string
        if ((tens_flag == "Y" or units_flag == "Y") and hundreds_flag == "N"):
            word_string += "and "
    if lakhs_flag == "Y":
        word_string += lakhs_word_string
        if ((tens_flag == "Y" or units_flag == "Y") and hundreds_flag == "N"):
            word_string += "and "
    if thousands_flag == "Y":
        word_string += thousands_word_string
        if ((tens_flag == "Y" or units_flag == "Y") and hundreds_flag == "N"):
            word_string += "and "
    if hundreds_flag == "Y":
        word_string += hundreds_word_string
        if (tens_flag == "Y" or units_flag == "Y"):
            word_string += "and "
    if tens_flag == "Y":
        word_string += tens_word_string
    if units_flag == "Y":
        word_string += units_word_string

    return word_string

def figs_to_words_imperial(input_number):
    word_string = "code under development"
    return word_string

def units_map(input_string):
    units_input_string = input_string[-1]
    for i in range(len(unit_figs)):
        if units_input_string == str((unit_figs[i])):
           units_conversion = str(unit_figs[i]) + " " + str(unit_words[i])
           units_return_string = str(unit_words[i])
           break
    return units_return_string

def tens_map(input_string):
    if int(input_string) in range(10, 20):
        tens_return_string = teens_map_1(input_string)
#        tens_return_string = teens_map_2(input_string)
    elif int(input_string) in range(20, 100):
        tens_return_string = other_tens_map(input_string)
    return tens_return_string

def teens_map_1(input_string):
#    print('teens map_1 using tuple')
    for i in range(len(teens_figs)):
        if input_string == str((teens_figs[i])):
            teens_return_string = str(teens_words[i])
            teens_conversion = str(teens_figs[i]) + " " + str(teens_words[i])
            break
    return teens_return_string

def teens_map_2(input_string):
#    print("teens_map_2 using dictionary")
    for x in word_map_3.keys():
       if input_string == str(x):
            teens_return_string = word_map_3[x]
            teens_conversion = str(x) + " " + str(teens_return_string)
            break
    return teens_return_string

def other_tens_map(input_string):
    if input_string[1] == '0':
        for x in word_map_2.keys():
            if input_string == str(x):
                tens_return_string = word_map_2[x]
                tens_conversion = str(x) + " " + str(tens_return_string)
                break
    else:
#        print("all other tens")
        tens_string_1 = input_string[0] + '0'
        tens_string_2 = input_string[1]
        for x in word_map_2.keys():
            if tens_string_1 == str(x):
                tens_word_1 = word_map_2[x]
                for x in word_map_1.keys():
                    if tens_string_2 == str(x):
                        tens_word_2 = word_map_1[x]
                        tens_return_string = str(tens_word_1) + " " + str(tens_word_2)
                        break
    return tens_return_string

def hundreds_map(input_string):
    hundred_fig = input_string[0]
    for x in word_map_1.keys():
       if hundred_fig == str(x):
            hundred_word = word_map_1[x]
            hundreds_return_string = str(hundred_word) + " " + hundreds
            break
    return hundreds_return_string

def thousands_map(input_string):
#    print('thousands_map ' + str(input_string))
    if int(input_string[0]) == 0:
        thousands_fig_1 = input_string[1]
        for x in word_map_1.keys():
            if thousands_fig_1 == str(x):
                thousands_word = word_map_1[x]
                thousands_return_string = str(thousands_word) + " " + thousands
                break
    else:
        thousands_fig_2 = input_string[0:2]
        thousands_word = tens_map(thousands_fig_2)
        thousands_return_string = str(thousands_word) + " " + thousands
    return thousands_return_string

def lakhs_map(input_string):
    if int(input_string[0]) == 0:
        lakhs_fig_1 = input_string[1]
        for x in word_map_1.keys():
            if lakhs_fig_1 == str(x):
                lakhs_word = word_map_1[x]
                lakhs_return_string = str(lakhs_word) + " " + lakh
#                print(lakhs_return_string)
                break
    else:
        lakhs_fig_2 = input_string
        lakhs_word = tens_map(lakhs_fig_2)
        lakhs_return_string = str(lakhs_word) + " " + lakhs
#        print(lakhs_return_string)
    return lakhs_return_string

def crores_map(input_string):
    if int(input_string[0]) == 0:
        crores_fig_1 = input_string[1]
        for x in word_map_1.keys():
            if crores_fig_1 == str(x):
                crores_word = word_map_1[x]
                crores_return_string = str(crores_word) + " " + crore
                break
    else:
        crores_fig_2 = input_string
        crores_word = tens_map(crores_fig_2)
        crores_return_string = str(crores_word) + " " + crores
    return crores_return_string

i = 1
#for x in input_file:
#    input_length = len(x.strip())
conversion_type = 'M'
for x in test_data:
    input_length = len(x)
    numeric_check = check_user_input(x)
    if numeric_check == 'Y':
        if input_length <= 9:
            if conversion_type == 'M':
                y = figs_to_words_metric(x)
            else:
                y = figs_to_words_imperial(x)
#                break
            print("figs : " + x + "  words : " + y)
            output_file.write(y)
        else:
            print("'" + x + "'" + " Invalid input. Can accept up to 9 digits only for now")
    else:
        print("'" + x + "'" + " Invalid input. Only integers allowed")

input_file.close()
output_file.close()
