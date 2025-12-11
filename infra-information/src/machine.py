from pydantic import BaseModel, field_validator
import json
import os
import logging


OS_LIST = ["ubuntu", "centos"]

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    handlers=[ 
        logging.FileHandler('./logs/log.log')  
    ]
    )

class Machine(BaseModel):
    name: str
    operating_system: str
    cpu: int
    ram: int
    storage: int

    @field_validator('name')
    @classmethod
    def validate_name(cls, name: str):
        if str(name) :
            return name
        else:
            raise ValueError('Name must be string')
        
    @field_validator('operating_system')
    @classmethod
    def validate_os(cls, operating_system: str):
        if str(operating_system).lower() in OS_LIST:
            return operating_system
        else:
            raise ValueError(f'please enter one of these os: {OS_LIST}')
        
    @field_validator('cpu')
    @classmethod
    def validate_cpu(cls, cpu: int):
        if int(cpu) and int(cpu) > 0 and int(cpu) < 100:
            return cpu
        else:
            raise ValueError('cpu must be a number between 0 - 100')
        
    @field_validator('ram')
    @classmethod
    def validate_ram(cls, ram: int):
        if int(ram) and int(ram) > 0 and int(ram) < 1000:
            return ram
        else:
            raise ValueError('ram must be a number between 0 - 1000')
        
    @field_validator('storage')
    @classmethod
    def validate_storage(cls, storage: int):
        if int(storage) and int(storage) > 0 and int(storage) < 10000:
            return storage
        else:
            raise ValueError('disk must be a number between 0 - 10000')
    
    def toDict(self):
        return {
        "name" : self.name,
        "OS" : self.operating_system,
        "CPU" : self.cpu,
        "RAM" : self.ram,
        "storage" : self.storage,
        }
    
    @classmethod    
    def create_machine(cls, name: str, operating_system: str, cpu: int, ram: int, storage: int, filename: str = "configs/machines.json"):
            """Create a machine instance and save it to a JSON file"""
            machine = cls(name=name, operating_system=operating_system, cpu=cpu, ram=ram, storage=storage)
            
            if os.path.exists(filename): # reading all items in the json file 
                with open(filename, 'r') as f:
                    machines = json.load(f)
            else:
                machines = []
            
            machines.append(machine.model_dump()) # creating a new list with the old and new data 
            
            with open(filename, 'w') as f: # writing to json file the new list of jsons
                json.dump(machines, f, indent=2)
            
            return machine
    
    
        
            
        
