# Library Management System
**This project is a small website that allows you to monitor your books, track profits and gains from selling and renting books, all through a simple and visually appealing interface.**

![image](https://github.com/user-attachments/assets/c3e3175b-3b2d-444f-aeb1-3554468180e3)

# Project Overview
**This Library Management System is built using Python (Flask), SQL, HTML, and CSS. It allows users to manage their books and keep track of sales and rentals. The website provides a clear visualization of your book inventory and related financial data.**

# Technologies Used
- Backend: Python (Flask)
- Frontend: HTML, CSS
- Database: SQL
- DevOps: Docker, GitHub Actions, Terraform, Ansible , AWS , AWS CLI

	## Docker
	![docker](https://github.com/user-attachments/assets/0141109b-92b2-4a5e-bf2a-e6e72cc140b9)

	**Docker is used to containerize the application, ensuring consistency across different environments. A Docker container includes everything the application needs to run: code, runtime, system tools, libraries, and settings.**

	## GitHub Actions
	![github actions](https://github.com/user-attachments/assets/78ad420c-2079-40d4-8e23-e947b2f3d030)

	**GitHub Actions automates, customizes, and executes software development workflows right in your repository. We use it for Continuous Integration and Continuous Deployment (CI/CD), enabling automated testing, building, and deployment.**

	## Terraform
	![terraform](https://github.com/user-attachments/assets/cd4c8ad7-0408-4b70-a4d6-2ec74c6531b9)

	**Terraform is used to create an EC2 instance on AWS, providing infrastructure as code. This allows us to define and provision the infrastructure in a safe and repeatable way.**
	
	## AWS CLI
	![aws cli](https://github.com/user-attachments/assets/aac46b76-4237-4eb6-9f32-8bb40d76b5a0)

	**The AWS CLI (Command Line Interface) is a unified tool that allows you to interact with AWS services directly from your command line. With AWS CLI, you can control multiple AWS services and automate tasks through scripts, making it 	easier and to manage resources like EC2 instances, S3 buckets, and more, without needing to use the AWS Management Console.**
	
	## Ansible
	![ansible](https://github.com/user-attachments/assets/c801ff06-8cec-4103-8cb6-189a7a5ddb46)

	**Ansible is employed for configuration management, automating the deployment and configuration of software on our EC2 instance.**

# Documentation Steps:
 ### Step 1: Clone the Repository
		git clone https://github.com/Mosami7/Devops_Depi.git
		cd Devops_Depi

 ### Step 2: Set Up a Virtual Environment
	python3 -m venv venv
	source venv/bin/activate

 ### Step 3: Install Dependencies
	pip install -r requirements.txt

 ### Step 4: Run the Application Locally
	export FLASK_APP=app.py
	flask run

 ### Step 5: Docker Installation
	sudo apt-get update
	sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

	sudo mkdir -p /etc/apt/keyrings
	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

	echo \
  	"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  	$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

	sudo apt-get update
	sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

 ### Step 6: Dockerize the Application
	#To build and run the Docker container:

	docker build -t mosami77/libimg .
	docker run -d --name libimg mosami77/libimg

 ### Step 7: Install AWS CLI
	curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
	unzip awscliv2.zip
	sudo ./aws/install

 ### Step 8: Configure AWS CLI
	aws configure
	#(put credentials from aws to ~/.aws/credentials in your local machine to connect terraform with aws)

 ### Step 9: Terraform Installation
	sudo apt-get update && sudo apt-get install -y gnupg software-properties-common curl
	curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
	echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
	sudo apt-get update && sudo apt-get install terraform

 ### Step 10: Using Terraform to Provision AWS EC2 Instances
	terraform init
	terraform apply

 ### Step 11: Ansible Installation
	sudo apt-get update
	sudo apt-get install ansible

 ### Step 12: Run Ansible Playbook
	ansible-playbook -i inventory playbook.yml

 > **Notes:**
 - > My DockerHub repo : https://hub.docker.com/repository/docker/mosami77/libimg
 - > Docker installation Resource : https://docs.docker.com/
 - > Terraform installtion Resource : https://developer.hashicorp.com/terraform/docs
 - > Ansible installation Resource : https://docs.ansible.com/
