""" Service requests for accessible objects """

from accessible_lib.scripts.accessible import accessible

ACC_OBJ = accessible('MSAA', "About Mozilla")
print ACC_OBJ.get_acc_name()
print ACC_OBJ.get_acc_role()
print ACC_OBJ.get_acc_value()
