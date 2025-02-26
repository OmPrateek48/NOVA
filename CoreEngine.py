# core/CoreEngine.py

import json
from core.MemoryManager import MemoryManager
from core.EvolutionManager import EvolutionManager
from core.AdminControl import AdminControl

class CoreEngine:
    def __init__(self):
        self.memory = MemoryManager()
        self.evolution = EvolutionManager()
        self.admin = AdminControl()

    def process_command(self, command, user_id):
        if self.admin.verify_admin(user_id):
            response = self.execute_admin_command(command)
        else:
            response = self.execute_user_command(command)
        return response

    def execute_admin_command(self, command):
        if command == "update_nova":
            return self.evolution.update_nova()
        elif command == "backup":
            return self.memory.create_backup()
        else:
            return "Unknown admin command"

    def execute_user_command(self, command):
        return f"NOVA received command: {command}"

if __name__ == "__main__":
    nova = CoreEngine()
    print(nova.process_command("backup", "OmPrateek4843"))  # Example Test
