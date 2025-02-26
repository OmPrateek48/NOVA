import shutil
import os
from datetime import datetime

BACKUP_DIR = "backups"

def create_backup():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_name = f"{BACKUP_DIR}/backup_{timestamp}.zip"
    shutil.make_archive(backup_name.replace(".zip", ""), 'zip', "./")
    print(f"Backup created: {backup_name}")

if __name__ == "__main__":
    create_backup()
