from src.machine import Machine

machines = []

def create_vm():
    while True:
        # print("what are your credentials?")
        # username = input("username:")
        # password = input("password:")
        print("machine info:")
        name = input("Name your vm:")
        while not Machine.validate_name(name):
            name = input("try again")
        os = input("operating system (Ubuntu/CentOs):")
        while not Machine.validate_os(os):
            os = input("try again")
        cpu = input("how much CPU do you want:")
        while not Machine.validate_cpu(cpu):
            cpu = input("try again")
        ram = input("how much RAM do you want:")
        while not Machine.validate_ram(ram):
            ram = input("try again")
        disk = input ("how much storage do you need in GB:")
        while not Machine.validate_disk(disk):
            disk = input("try again")
        # Create and save the machine
vm = Machine.create_vm(name=name, os=os, cpu=cpu, ram=ram, disk=disk)
machines.append(vm)
print(f"Machine created successfully: {machine}\n")
        
