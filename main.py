import os
import sys
import subprocess


def change_color(folder, icon):
    desktop_ini = os.path.join(folder, "desktop.ini")

    with open(desktop_ini, "w") as file:
        file.write("[.ShellClassInfo]\n")
        file.write(f"IconResource={icon},0\n")

    subprocess.call(["attrib", "+h", "+s", desktop_ini]) #desktop.ini file hide

    subprocess.call(["attrib", "+r", folder]) #folder lock


if __name__ == "__main__":
    folder = sys.argv[1]
    color = sys.argv[2]

    base_dir = os.path.dirname(sys.argv[0])
    icon = os.path.join(base_dir, "Icons", f"{color}.ico")

    change_color(folder, icon)
    