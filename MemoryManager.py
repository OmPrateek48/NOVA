# core/MemoryManager.py

import json
import os

class MemoryManager:
    def __init__(self, file_path="storage/nova_memory.json"):
        self.file_path = file_path
        self.memory = self.load_memory()

    def load_memory(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                return json.load(file)
        return {}

    def save_memory(self):
        with open(self.file_path, "w") as file:
            json.dump(self.memory, file, indent=4)

    def update_memory(self, key, value):
        self.memory[key] = value
        self.save_memory()

    def create_backup(self):
        backup_file = self.file_path.replace(".json", "_backup.json")
        with open(backup_file, "w") as file:
            json.dump(self.memory, file, indent=4)
        return f"Backup created at {backup_file}"
