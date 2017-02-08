""" Service requests for accessible objects """

from accessible_lib.scripts.accessible import accessible

acc_obj = accessible('MSAA', "About Mozilla")
print(acc_obj.get_acc_name())
print(acc_obj.get_acc_role())
