from machine import Machine
from pydantic import ValidationError
import logging
import subprocess

machines = []
OS_LIST = ["ubuntu", "centos"]

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    handlers=[ 
        logging.FileHandler('./logs/log.log')  
    ]
)


def user_input():
    while True:
        choice = input("Do you want to create a VM? (y=yes, n=no): ").lower()
        
        if choice == 'n':
            print("Exiting...")
            break
        elif choice != 'y':
            print("Invalid choice. Please enter 'y' or 'n'.")
            continue
        logging.info("starting machine creation")
        # name
        name = None
        while name is None:
            logging.info("naming the machine...")
            name_input = input("enter your machines name: ")
            try:
                Machine(name=name_input, operating_system='ubuntu', cpu=1, ram=1, storage=1)
                name = name_input
                logging.info(f"name for the machine {name}")
            except ValidationError as e:
                error_msg = e.errors()[0]['msg']
                print(f"Error: {error_msg}")
                logging.error(f"Error: {error_msg}")

        # OS
        operating_system = None
        while operating_system is None:
            logging.info("creating os...")
            os_input = input(f"enter your machines operating system ({', '.join(OS_LIST)}): ")
            try:
                Machine(name="Valid", operating_system=os_input, cpu=1, ram=1, storage=1)
                operating_system = os_input
                logging.info(f"os for {name} is {operating_system}")
            except ValidationError as e:
                error_msg = e.errors()[0]['msg']
                print(f"Error: {error_msg}")
                logging.error(f"Error: {error_msg}")

        # cpu
        cpu = None
        while cpu is None:
            logging.info("creating cpu...")
            cpu_input = input("cpu: ")
            try:
                cpu_value = int(cpu_input)
                Machine(name="Valid", operating_system='ubuntu', cpu=cpu_value, ram=1, storage=1)
                cpu = cpu_value
                logging.info(f"cpu for {name} is {cpu}")
            except ValueError:
                print(f"Error: Invalid cpu format. Please enter a number.")
                logging.error("didn't insert a numbers to the cpu field")
                continue
            except ValidationError as e:
                error_msg = e.errors()[0]['msg']
                print(f"Error: {error_msg}")
                logging.error(f"Error: {error_msg}")

        # ram
        ram = None
        while ram is None:
            logging.info("creating ram...")
            ram_input = input("ram: ")
            try:
                ram_value = int(ram_input)
                Machine(name="Valid", operating_system='ubuntu', cpu=1, ram=ram_value, storage=1)
                ram = ram_value
                logging.info(f"ram for {name} is {ram}")
            except ValueError:
                print(f"Error: Invalid ram format. Please enter a number.")
                logging.error("didn't insert a numbers to the ram field")
                continue
            except ValidationError as e:
                error_msg = e.errors()[0]['msg']
                print(f"Error: {error_msg}")
                logging.error(f"Error: {error_msg}")

        # storage
        storage = None
        while storage is None:
            logging.info("creating storage...")
            storage_input = input("storage: ")
            try:
                storage_value = int(storage_input)
                Machine(name="Valid", operating_system='ubuntu', cpu=1, ram=1, storage=storage_value)
                storage = storage_value
                logging.info(f"storge for {name} is {storage}")
            except ValueError:
                print(f"Error: Invalid storage format. Please enter a number.")
                logging.error("didn't insert a numbers to the storage field")
                continue
            except ValidationError as e:
                error_msg = e.errors()[0]['msg']
                print(f"Error: {error_msg}")
                logging.error(f"Error: {error_msg}")

        vm = Machine.create_machine(name=name, operating_system=operating_system, cpu=cpu, ram=ram, storage=storage)
        print(f"Machine created successfully: {vm}\n")
        logging.info(f"machine created successfully: {vm}\n")

def install_nginx():
    try:
        result = subprocess.run(["bash","scripts/install_ngnix.sh"], check=True, capture_output=True)
        print(result.stdout.decode())
        logging.info("servcie installed successfully")
    except subprocess.CalledProcessError as err:
        print("script failed with error:", err.stderr)
        logging.error("failed to install nginx: %s", err)

def main():
    user_input()
    install_nginx()

main()
