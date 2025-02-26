# AdminControl.py

class AdminControl:
    def __init__(self):
        self.admin_id = "OmPrateek4843"  # Master Key

    def verify_admin(self, user_id):
        return str(user_id) == self.admin_id  # Ensure user_id is compared as a string

# Create an instance of AdminControl
admin_control = AdminControl()

# Function to check if a user is an admin
def is_admin(user_id):
    return admin_control.verify_admin(user_id)
