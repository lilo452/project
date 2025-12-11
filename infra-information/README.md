# Infra Automation

Infra Automation is a Python-based tool that simulates infrastructure provisioning by interactively collecting virtual machine (VM) definitions, validating them using Pydantic, and preparing each VM for configuration with an automated setup script.  
This project serves as the foundation for future infrastructure-as-code automation using cloud providers and Terraform.

## Features

* **Interactive VM creation**: The user is prompted to enter details for each VM.
* **Pydantic validation**: All inputs are validated to ensure correct structure and data types.
* **JSON configuration output**: All validated VM definitions are saved to a structured JSON file.
* **Service installation via Bash**: After each VM is provisioned, a script is triggered to simulate installing and configuring **nginx** (theoretically).
* **Modular Python design**: Code is organized using classes and separate modules for improved maintainability.

## VM Fields Collected

For every machine, the tool collects:

* **Machine Name** – The unique name of the VM.
* **Operating System** – Example: Ubuntu, CentOS.
* **CPU** – Number of virtual CPU cores.
* **RAM** – Amount of memory in GB.
* **Storage** – Disk allocation size in GB.
  
Each field is fully validated using a Pydantic model to prevent malformed configurations.

## Workflow

1. Run the program.
2. The CLI prompts the user for VM information.
3. Pydantic validates the input.
4. Valid VM definitions are saved into the `instances.json` file.
5. A post-provisioning script runs to simulate installing **nginx** on the machine (theoretically).

## Requirements

* Python 3.10+
* Virtual environment
* Pydantic (v2)

## Running the Program

```bash
python3 -m venv venv
source venv/bin/activate
pip install pydantic
python3 infra_simulator.py
```

## Json output

The resulting files may look like:

```json
[
  {
    "name": "web-server-01",
    "os": "Ubuntu",
    "cpu": 4,
    "ram": 16,
    "storage": 100
  }
]
```
## Script Execution (nginx Installation)

After each VM is successfully provisioned, the application runs a setup script that installs **nginx** and performs initial configuration.

* Example steps performed:

* Updating package repositories

* Installing the nginx package

* Printing success messages

* Writing logs to track the process

## Project Structure

```
infra-simulator/
|-- scripts/
|-- configs/
|-- logs/
|-- src/
|-- README.md
```

## Future Enhancements

* Integration with AWS for real provisioning

* Terraform automation for VM creation

* Retrieve and use VM IP addresses

* Install nginx on actual created instances

* Add more advanced configuration steps and service setup