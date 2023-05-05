# network_scanner
My own custom network scanner script.

Usage:
-In your command console navigate to the folder where you store the script.
-Use the command 'python network_scanner.py -t <IP RANGE>' ( IP RANGE = for example 10.10.1.1/24)

Output:
It will show a table with the IPs and MAC Address of all found devices like this:

IP             MAC Address
---------------------------
10.10.1.5       11:22:33:44:55:66
10.10.1.10      11:22:33:44:66:77


Arguments:
-t or --target =  IP target range
-h or --help = to display the help

Enjoy!
