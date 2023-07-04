__all__ = ['random_string',]





import secrets
import string
import math





class __ErrorHandling():
    
    def _random_string_error_handler(length,regex,only_letters,only_digits):
        #length
        if (length_type:=type(length)) is not int:
            error = "Value must be int not {}".format("".join(str(length_type).split("'")[1:-1]))
            raise ValueError(error)
        elif length<1:
            error = f"Length must be greater than 0. The Given length {length} is {int(math.fabs(length))+1} short."
            raise IndexError(error)
        #end length



        ##############
        #regex
        elif regex :
            if type(regex) is not str:
                error = "Regex must be a string. example: 'AaBb123#$' "
                raise ValueError(error)
        #end regex

        #only letters or digits
        elif (letter_type:=type(only_letters)) is not bool:
            error = "Value for only_letters must be boolean not {}".format("".join(str(letter_type).split("'")[1:-1]))
            raise ValueError(error)
        elif (digits_type:=type(only_digits)) is not bool:
            error = "Value for only_digits must be boolean not {}".format("".join(str(digits_type).split("'")[1:-1]))
            raise ValueError(error)
        
        #Disallowing from using regex and only_letters and only_digits at the same time.
        if sum([bool(regex),only_letters,only_digits]) > 1:
            values = {'regex':bool(regex),'only_letters':only_letters,'only_digits':only_digits}
            variable_names = " and ".join([variable for variable,value in values.items() if value==True])
            error = f"can't use {variable_names} at the same time."
            raise TypeError(error)

        ##############





def random_string(length:int=15,regex:str=False,only_letters:bool=False,only_digits:bool=False):
    __ErrorHandling._random_string_error_handler(length,regex,only_letters,only_digits)
    #characters
    if not regex:
        #only letters or digits or both
        if only_letters == True:
            characters = string.ascii_letters
        elif only_digits == True:
            characters = string.digits
        else:
            characters = string.hexdigits
    else:
        characters = regex

    

    generated_string = "".join([secrets.choice(characters) for _ in range(length)])
    return generated_string
