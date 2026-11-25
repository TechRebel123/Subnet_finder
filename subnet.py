get = str(input("Enter your IP(x.x.x.x/(1-32)): "))
split = get.split("/")
ip = split[0]
on_bits = split[1]
off_bits = 32-int(on_bits)
hosts = (2**off_bits) - 2
ip_split = ip.split(".")

if int(on_bits) > 24 and int(on_bits) <= 32:
    subnet = "255.255.255." + str(256-2**int(off_bits))
elif int(on_bits) > 16 and int(on_bits) <= 24:
    subnet = "255.255." + str(256-2**(int(off_bits) - 8)) + ".0"
elif int(on_bits) > 8 and int(on_bits) <= 16:
    subnet = "255." + str(256-2**(int(off_bits) - 16)) + ".0.0"
elif int(on_bits) >= 1 and int(on_bits) <= 8:
    subnet = str(256-2**(int(off_bits) - 24)) + ".0.0.0"
else:
    print("Invalid subnet!")
    raise SystemExit
print("IP: ", get)
print("Number of hosts: ", hosts)
print("Subnet: ", subnet)
