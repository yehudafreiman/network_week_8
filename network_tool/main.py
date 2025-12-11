from network_tool.core.utils import *
from network_tool.core.output_string import *


if __name__ == "__main__":

    ip_str = input_ip()
    mask_str = input_subnet_mask()
    class_type = identify_class_type()
    network_address = calculate_network_address(ip_str, mask_str)
    broadcast_address = calculate_broadcast_address(ip_str, mask_str)
    num_hosts = calculate_num_hosts(network_address, broadcast_address)
    cidr = calculate_cidr_mask(mask_str)

    def export_to_txt():
        with open(f"subnet_info_{ip_str}_205368319.txt", "w") as f:

            f.write(format_input_ip(ip_str))
            f.write(format_subnet_mask(mask_str))
            f.write(format_classful_status(class_type))
            f.write(format_network_address(network_address))
            f.write(format_broadcast_address(broadcast_address))
            f.write(format_num_hosts(num_hosts))
            f.write(format_cidr_mask(cidr))


    export_to_txt()
