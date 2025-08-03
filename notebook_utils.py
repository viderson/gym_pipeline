import sys
import os

def bootstrap_project_root(levels_up=1):
    project_root = os.path.abspath(os.path.join(os.getcwd(), *[".."] * levels_up))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
