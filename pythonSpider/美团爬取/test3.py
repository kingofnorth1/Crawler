
ip_list = []
port_list = []
with open("ipPort.txt","r") as f:
    for line in f.readlines(1):
        line = line.strip("\n")
        ip_list.append(line.split(" ")[0])
        port_list.append(line.split(" ")[1])
print(ip_list,port_list)

for i in range(0,len(ip_list)):
    print(ip_list[i]+":"+port_list[i])
