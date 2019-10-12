import json
from user import User
from file_account import FileAccount
from cli_interface import CliInterface

if __name__ == '__main__':
    app = CliInterface()
    app.main_menu()
    app.manage_menu()
    #new_user = User().new_account('lala', 'lolo')
    #existing_user = User()
    #existing_user.existing_account('lala', 'lolo')
    #existing_user = existing_user.existing_account('lala', 'lolo')
    #file_account = FileAccount(existing_user.get_cipher(), existing_user.get_filename())
    #file_account.list_all_accounts()
    #file_account.remove_entry("ttest_account")
    # #create_account('lala', 'lolo')
    # res = read_json("account_lala","lala","lolo")
    # print(res)
    # new_account = account_details("id1", "toto", '"blabla"')
    # print(new_account)
    #file_account.add_entry("test_account","toto","tata", json.dumps("test"))
    #file_account.display_all_accounts()
    #print(file_account.get_all_accounts())
    # #res = add_entry(res, "new", "test")
    # print(res["accounts"])
    # #print(res)
    #
    # save('account_lala', json.dumps(res), 'lala', 'lolo')
