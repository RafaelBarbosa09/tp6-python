import psutil

status = psutil.net_if_stats()
interfaces = psutil.net_if_addrs()
nomes = []

# Obtém os nomes das interfaces primeiro
for i in interfaces:
    nomes.append(str(i))

# Depois, imprimir os valores:
for i in nomes:
    print(i+":")
    for j in interfaces[i]:
        print("\t"+str(j))

print("\n")
print("*"*70)

for i in nomes:
    print(i)
    print("\t"+str(status[i]))
