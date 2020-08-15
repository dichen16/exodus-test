import subprocess


def check_installed_pkg(pkg):
    cmd = "rpm -q " + pkg
    # The run() function was added in Python 3.5
    res = subprocess.run(cmd, shell=True, capture_output=True)
    if res.returncode:
        return False
    return True

