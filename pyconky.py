#!/usr/bin/python3
import socket
import fcntl
import struct
import netifaces as ni

# given an interface name( Ex: wlan0), return the IP address 
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15].encode('ascii'))
    )[20:24])
# this is the main function  
# It reads the input file until if finds the NETWORK section, then
# parses the next line, which should be a generice definition of a 
# description of a network interface and associated IP address.
# It then finds all of the wired and wireless interfaces that have
# IP addresses and adds them to the NETWORK section
def read_file_until_network(filename, output_filename):
  with open(filename, "r") as f:
    with open(output_filename, "w") as out:
      for line in f:
        if "NETWORK" in line:
          out.write(line)
          break
        else:
          out.write(line)
      line = f.readline()
      template=line
      fields=template.split()
      n=len(fields)
      toRep = fields[n-1]
      fields[n-1]="lo"+"}"

      lst = ni.interfaces()

      addresses={}
      for string in lst:
        ip_address = get_ip_address(string)
        if ip_address:
            addresses[string]=ip_address
        else:
            print(f"Unable to find IP address for {string}")
      for addr in addresses:
          x = addr[0:1]
          if addr[0:1] == 'e':
              ip = addresses[addr] 
              if ip:
                  fields[n-1]=addr+"}"

                  str = " ".join(fields)
                  str = str.replace("Wireless","Wired")
                  out.write(str+"\n")

          if addr[0:1] == 'w':
              ip = addresses[addr] 
              if ip:
                  fields[n-1]=addr+"}"

                  str = " ".join(fields)
                  out.write(str+"\n")

      for line in f:
          out.write(line)
      
      

def main():
  input_filename = ".cronkyrc"
  output_filename = "cronkyrc.txt"
  read_file_until_network(input_filename, output_filename)

if __name__ == "__main__":
  main()
