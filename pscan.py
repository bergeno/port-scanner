import socket

ports = [];
count = 1;
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
client.settimeout(0.05);

numberOfPorts = int(input("How many ports do you want to scan? "));
ip = input("Choose the host or ip address: ");


while count <= numberOfPorts:
    port = int(input("{} - Choose the port: ".format(count)));
    ports.append(port)
    count += 1;

for port in ports:
    code = client.connect_ex((ip, port));

    if code == 0:
        print("-> Port  {} is open" .format(port));
    else:
        print("-> Port {} is close." .format(port));    

print("Scan completed")
