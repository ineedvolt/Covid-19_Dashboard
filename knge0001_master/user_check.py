# List which contains the login information of the super users
superUserList = ["admin@admin.com"]
userEmail = []


def check_superuser(email):
    is_superuser = False
    # Check if the input email is inside the superUserList
    if email in superUserList:
        # If True, return flag as True
        is_superuser = True
    return is_superuser
