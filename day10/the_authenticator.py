user = "admin"
def admin_required(func):
    def wrapper (*args):
        global user
        if user != "admin":
            raise PermissionError
        else:
            func(*args)
    return wrapper
@admin_required
def check_pass():
    print(f"abrar365")
check_pass()