# core/EvolutionManager.py

import os

class EvolutionManager:
    def __init__(self):
        self.update_file = "updates/nova_updates.py"

    def update_nova(self):
        if os.path.exists(self.update_file):
            try:
                exec(open(self.update_file).read())
                return "NOVA has been updated successfully!"
            except Exception as e:
                return f"Update failed: {str(e)}"
        return "No update file found."
