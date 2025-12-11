

def input_ip():
    ip = input("Enter ip address like 192.168.10.130, any octet between 0-255: ")
    return ip

def input_subnet_mask():
    subnet_mask = input("Enter subnet mask like 255.255.255.192, any octet between 0-255: ")
    return subnet_mask


def validate_ip(ip):
    return

def validate_subnet_mask(subnet_mask):
    return

def converse_address(address):
    split_address = address.split('.')
    result = list(map(int, split_address))
    return result

def calculate_block_size(subnet_mask):
    block_size = 256 - subnet_mask[-1]
    return block_size

def identify_class_type():
    return

def calculate_network_address(ip, subnet_mask):
    ip_list = converse_address(ip)
    subnet_mask_list = converse_address(subnet_mask)
    network_address = []
    block_size = calculate_block_size(subnet_mask_list)

    for i in range(len(subnet_mask_list)):
        if subnet_mask_list[i] == 255:
            network_address.append(ip_list[i])
        if subnet_mask_list[i] == 0:
            network_address.append(0)
        if subnet_mask_list[i] != 255 and subnet_mask_list[i] != 0:
            network_address.append((ip_list[i] // block_size) * block_size)

    return network_address


def calculate_broadcast_address(ip, subnet_mask):
    ip_list = converse_address(ip)
    subnet_mask_list = converse_address(subnet_mask)
    broadcast_address = []
    block_size = calculate_block_size(subnet_mask_list)
    network_address = calculate_network_address(ip, subnet_mask)

    for i in range(len(subnet_mask_list)):
        if subnet_mask_list[i] == 255:
            broadcast_address.append(ip_list[i])
        if subnet_mask_list[i] == 0:
            broadcast_address.append(255)
        if subnet_mask_list[i] != 255 and subnet_mask_list[i] != 0:
            broadcast_address.append((network_address[i] + block_size) -1)

    return broadcast_address

def calculate_num_hosts(network_address, broadcast_address):
    first_host = network_address[-1] -1
    last_host = broadcast_address[-1] -1
    return last_host - first_host

def calculate_cidr_mask(subnet_mask):
    list_subnet_mask = converse_address(subnet_mask)
    placed_value = [1023, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    binary = []

    for v in range(len(placed_value)):
        for i in range(len(list_subnet_mask)):
            if list_subnet_mask[i] >= v:
                binary.append('1')
                list_subnet_mask[i] -= v
            else:
                binary.append('0')

    total = 0
    for j in range(len(binary)):
        if binary[j] == 1:
            total += 1

    return total




