## Python 3.x

from winreg import *

reg_path = r'SOFTWARE'
mid_reg_path = r'SOFTWARE\\Mid'
full_reg_path = r"SOFTWARE\\Mid\\Full"
key = 'This is a key'

def Check_Key():
    ## Create a handle
    reg_key = OpenKey(HKEY_CURRENT_USER, full_reg_path, 0, KEY_READ)

    ## Check if key existed
    try:
        keyValue = EnumValue(reg_key, 0)
        reg_key.Close()

        ## Check if keycode is correct
        if keyValue[1]!=key:
            Create_Value()
    except:
        Create_Key()
        Create_Value()

def Create_Key():
    reg_key = OpenKey(HKEY_CURRENT_USER, reg_path, 0, KEY_READ)
    CreateKey(reg_key, "Mid")
    reg_key.Close()
    
    reg_key = OpenKey(HKEY_CURRENT_USER, mid_reg_path, 0, KEY_READ)
    CreateKey(reg_key, "Full")
    reg_key.Close()

def Create_Value():
    reg_key = OpenKey(HKEY_CURRENT_USER, full_reg_path, 0, KEY_SET_VALUE)
    SetValueEx(reg_key, "Key", 0, REG_SZ, key)
    reg_key.Close()

if __name__=='__main__':
    Check_Key()
