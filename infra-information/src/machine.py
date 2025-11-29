from pydantic import BaseModel, field_validator

os_list = ["ubuntu", "centos"]

class Machine(BaseModel):
    name: str
    os: str
    cpu: int
    ram: int
    disk: int

    @field_validator('name')
    def validate_name(name: str):
        if str(name) :
            return True
        else:
            raise ValueError('Name must be string')
        
    @field_validator('os')
    def validate_name(os: str):
        if str(os).lower() in os_list:
            return True
        else:
            raise ValueError(f'please enter one of these os: {os_list}')
        
    @field_validator('cpu')
    def validate_cpu(cpu: int):
        if int(cpu) and int(cpu) > 0 and int(cpu) < 100:
            return True
        else:
            raise ValueError('cpu must be a number between 0 - 100')
        
    @field_validator('ram')
    def validate_ram(ram: int):
        if int(ram) and int(ram) > 0 and int(ram) < 1000:
            return True
        else:
            raise ValueError('ram must be a number between 0 - 1000')
    @field_validator('disk')
    def validate_disk(disk: int):
        if int(disk) and int(disk) > 0 and int(disk) < 10000:
            return True
        else:
            raise ValueError('disk must be a number between 0 - 10000')
        
