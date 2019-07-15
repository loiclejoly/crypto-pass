from Cipher import AESCipher
from getpass import getpass
import json
from User import User
from FileAccount import FileAccount


def fix_binary_data_length(binary_data):
    """
    Right padding of binary data with 0 bytes
    Fix "ValueError: The length of the provided data is not a multiple of the block length."
    """
    block_length = 16
    binary_data_length = len(binary_data)
    length_with_padding = (
            binary_data_length + (block_length - binary_data_length) % block_length
    )
    return binary_data.ljust(length_with_padding, b"\0"), binary_data_length


if __name__ == '__main__':
    #new_user = User().new_account('lala', 'lolo')
    existing_user = User()
    existing_user.existing_account('lala', 'lolo')
    #existing_user = existing_user.existing_account('lala', 'lolo')
    file_account = FileAccount(existing_user.get_cipher(), existing_user.get_filename())
    #file_account.list_all_accounts()
    #file_account.remove_entry("ttest_account")
    # #create_account('lala', 'lolo')
    # res = read_json("account_lala","lala","lolo")
    # print(res)
    # new_account = account_details("id1", "toto", '"blabla"')
    # print(new_account)
    file_account.add_entry("test_account","toto","tata", json.dumps("test"))
    # #res = add_entry(res, "new", "test")
    # print(res["accounts"])
    # #print(res)
    #
    # save('account_lala', json.dumps(res), 'lala', 'lolo')
