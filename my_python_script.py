import os

workspace = os.environ.get('WORKSPACE')
if workspace:
    print(f"Workspace: {workspace}")
else:
    print("WORKSPACE environment variable not set.")
