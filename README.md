# Ephemeral Cloud-Native Lab Deployer 🧪

A command-line interface (CLI) tool designed to easily spin up, manage, and tear down various containerized cybersecurity lab environments using Docker and Docker Compose.

This tool simplifies the process of starting labs for security practice, research, or CTFs, allowing you to focus on learning without complex setup procedures.

## ✨ Features

* **List Labs:** Quickly see all available lab environments.
* **Start & Stop:** Easily deploy and shut down entire lab environments with single commands.
* **Status Check:** View the real-time status of all containers within a specific lab.
* **Resource Management:** A simple command to clean up unused Docker containers, networks, and volumes to free up system resources.
* **Extensible:** Adding new labs is as simple as creating a new Docker Compose file in the `labs` directory.

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Make sure you have the following software installed:

* **Python 3.x**
* **Docker:** [Installation Guide](https://docs.docker.com/engine/install/)
* **Docker Compose:** [Installation Guide](https://docs.docker.com/compose/install/)

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/DivInstance/ephermal-lab-deployer.git
    cd ephermal-lab-deployer
    ```

2.  **Install Python dependencies:**
    It's recommended to use a virtual environment.
    ```sh
    # Create and activate a virtual environment (optional but recommended)
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

    # Install required packages
    pip install click
    ```

3.  **Run using your command-line interface :**
    From the root folder run 
    ```sh
    python cli.py
    ```



### 🛠️ Usage

All commands are run from the terminal in the project's root directory.

* **List all available labs:**
    ```sh
    python cli.py list
    ```

* **Start a lab environment:** (e.g., `metasploit-android`)
    ```sh
    python cli.py start metasploit-android
    ```

* **Check the status of a running lab:**
    ```sh
    python cli.py status metasploit-android
    ```

* **Stop and remove a lab's containers:**
    ```sh
    python cli.py stop metasploit-android
    ```

* **Clean up all unused Docker resources:**
    ```sh
    python cli.py cleanup
    ```



## Command-Line Interface Workflow Example

```console
divyaranjansahoo@IhsuhK:/ephermal-lab-deployer $ python -m cli --help
Usage: cli.py [OPTIONS] COMMAND [ARGS]...
  Ephemeral Cloud Native Lab Deployer 🧪 A CLI tool to manage security lab
  environments using Docker.
Options:
  --help  Show this message and exit.
Commands:
  cleanup  Removes all unused Docker networks, containers, and volumes.
  list     Lists all available lab environments.
  start    Starts a specific lab environment in the background.
  status   Shows the status of containers for a specific lab.
  stop     Stops and removes all containers for a specific lab.
  
divyaranjansahoo@IhsuhK:/ephermal-lab-deployer $ python -m cli list
📚 Available Labs:
  - sql-injection
  - web-vulnerability
  - metasploit-android
  
divyaranjansahoo@IhsuhK:/ephermal-lab-deployer $ python -m cli start metasploit-android
🚀 Starting lab: metasploit-android...
⏳ Please wait, this may take several minutes if images need to be downloaded...
✅ Lab 'metasploit-android' deployed successfully!
   - Connect to the device with: adb connect localhost:5555

divyaranjansahoo@IhsuhK:/ephermal-lab-deployer $python -m cli status metasploit-android 
📊 Checking status for lab: metasploit-android...
NAME             IMAGE                                             COMMAND                  SERVICE      CREATED          STATUS          PORTS
metasploit-lab   metasploitframework/metasploit-framework:latest   "docker/entrypoint.s…"   metasploit   23 minutes ago   Up 5 minutes    0.0.0.0:55553->4444/tcp, [::]:55553->4444/tcp


divyaranjansahoo@IhsuhK:/ephermal-lab-deployer $python -m cli stop metasploit-android 
python cli.py stop metasploit-android
🛑 Stopping lab: metasploit-android...
✅ Lab 'metasploit-android' has been stopped and cleaned up.
```


> **Note:**  
> `python cli.py` and `python -m cli` work almost the same way.  
> The difference is that the second command runs the script as a **module**.  
> You can use either command, I generally use `python -m`, so don't get confused.



## 🧑‍💻 Author

**Divyaranjan Sahoo**
CSE Student & Cybersecurity Enthusiast

🌐 **Links:**

* [Portfolio](https://divyaranjansahoo.vercel.app/)
* [GitHub](https://github.com/DivInstance)
* [LinkedIn](https://linkedin.com/in/divyaranjansahoo)

📧 **Contact:** divyaranjan20175@gmail.com

## 📄 License

This project is proprietary and all rights are reserved. Please see the [LICENSE](LICENSE) file for more details.
```eof