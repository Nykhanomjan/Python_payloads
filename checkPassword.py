import string
def check_password_strength(password):
    length_cnt=len(password)
    isUpper=False
    isLower=False
    isNumber=False
    isSpecial=False
    for data in password  :
        if(data.isupper()):
            isUpper=True
        if(data.islower()):
            isLower=True
        if(data.isdigit()):
            isNumber=True
        if data in string.punctuation:
            isSpecial=True
    condition_cnt=isLower+isUpper+isNumber+isSpecial
    if length_cnt>=12 and  condition_cnt==4:
        return 'Strong'
    elif length_cnt>=8 and condition_cnt>=3:
        return 'Medium'
    else:
        return 'Weak'
print(check_password_strength("MyPassword123!"))
print(check_password_strength("asdsadasdasdadD.222"))
print(check_password_strength("weakpass"))

        