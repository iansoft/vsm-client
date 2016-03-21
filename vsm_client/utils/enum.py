# -*- coding:utf-8 –*-


class Group():
    admin = "admin"
    conductor = "conductor"


class BaseStatus():
    OK = 0
    error = 1
    warning = 2


class AccountStatus(BaseStatus):
    exist_user = 4



