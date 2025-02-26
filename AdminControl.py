# core/AdminControl.py

class AdminControl:
    def __init__(self):
        self.admin_id = "OmPrateek4843"  # Master Key

    def verify_admin(self, user_id):
        return user_id == self.admin_id
