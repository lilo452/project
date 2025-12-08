from pydantic import BaseModel, field_validator, ValidationError
import json
import os

OS_LIST = ['ubuntu', 'windows']

# ----------- the machine class ----------------- #
class Machine(BaseModel):
    name: str
    os: str
    cpu: int
    ram: int
    storage: int
    
    @field_validator('name')
    @classmethod
    def validate_name(cls, v: str) -> str:
        if not str(v):
            raise ValueError('Name must be a string')
        return v
    
    @field_validator('os')
    @classmethod
    def validate_os(cls, v: str) -> str:
        if not v.lower() in OS_LIST:
            raise ValueError(f'OS must be one of {OS_LIST}')
        return v.lower()
    
    @field_validator('cpu')
    @classmethod
    def validate_cpu(cls, v: int) -> int:
        if not 0 <= v <= 100:
            raise ValueError('Cpu must be between 0 and 100')
        return v
    
    @field_validator('ram')
    @classmethod
    def validate_ram(cls, v: int) -> int:
        if not 0 <= v <= 1000:
            raise ValueError('Ram must be between 0 and 1000')
        return v
    
    @field_validator('storage')
    @classmethod
    def validate_storage(cls, v: int) -> int:
        if not 0 <= v <= 10000:
            raise ValueError('Storage must be between 0 and 10000')
        return v
    
    @classmethod
    def create_machine(cls, name: str, operating_system: str, cpu: int, ram: int, storage: int, filename: str = "machines.json"):
        """Create a machine instance and save it to a JSON file"""
        machine = cls(name=name, os=operating_system, cpu=cpu, ram=ram, storage=storage)
        
        if os.path.exists(filename): # reading all items in the json file 
            with open(filename, 'r') as f:
                machines = json.load(f)
        else:
            machines = []
        
        machines.append(machine.model_dump()) # creating a new list with the old and new data 
        
        with open(filename, 'w') as f: # writing to json file the new list of jsons
            json.dump(machines, f, indent=4)
        
        return machine

# ----------- Main loop ---------------- #
while True:
    choice = input("Do you want to create a VM? (y=yes, n=no): ").lower()
    
    if choice == 'n':
        print("Exiting...")
        break
    elif choice != 'y':
        print("Invalid choice. Please enter 'y' or 'n'.")
        continue
    
    # name
    name = None
    while name is None:
        name_input = input("enter your machines name: ")
        try:
            Machine(name=name_input, os='windows', cpu=1, ram=1, storage=1)
            name = name_input
        except ValidationError as e:
            error_msg = e.errors()[0]['msg']
            print(f"Error: {error_msg}")

    # OS
    os_choice = None
    while os_choice is None:
        os_input = input(f"enter your machines operating system ({', '.join(OS_LIST)}): ")
        try:
            Machine(name="Valid", os=os_input, cpu=1, ram=1, storage=1)
            os_choice = os_input
        except ValidationError as e:
            error_msg = e.errors()[0]['msg']
            print(f"Error: {error_msg}")

    # cpu
    cpu = None
    while cpu is None:
        cpu_input = input("cpu: ")
        try:
            cpu_value = int(cpu_input)
            Machine(name="Valid", os='windows', cpu=cpu_value, ram=1, storage=1)
            cpu = cpu_value
        except ValueError:
            print(f"Error: Invalid cpu format. Please enter a number.")
        except ValidationError as e:
            error_msg = e.errors()[0]['msg']
            print(f"Error: {error_msg}")

    # ram
    ram = None
    while ram is None:
        ram_input = input("ram: ")
        try:
            ram_value = int(ram_input)
            Machine(name="Valid", os='windows', cpu=1, ram=ram_value, storage=1)
            ram = ram_value
        except ValueError:
            print(f"Error: Invalid ram format. Please enter a number.")
        except ValidationError as e:
            error_msg = e.errors()[0]['msg']
            print(f"Error: {error_msg}")

    # storage
    storage = None
    while storage is None:
        storage_input = input("storage: ")
        try:
            storage_value = int(storage_input)
            Machine(name="Valid", os='windows', cpu=1, ram=1, storage=storage_value)
            storage = storage_value
        except ValueError:
            print(f"Error: Invalid storage format. Please enter a number.")
        except ValidationError as e:
            error_msg = e.errors()[0]['msg']
            print(f"Error: {error_msg}")

    # Create and save the machine
    machine = Machine.create_machine(name=name, operating_system=os_choice, cpu=cpu, ram=ram, storage=storage)
    print(f"Machine created successfully: {machine}\n")