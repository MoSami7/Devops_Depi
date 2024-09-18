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

 	## Kubernetes
	![K8](https://github.com/user-attachments/assets/edcd76cc-944b-4286-b1f8-23c811a04e86)

	**Kubernetes (or K8s) is an open-source platform designed to automate deploying, scaling, and operating application containers. It helps you manage containerized applications in a clustered environment, ensuring 	that your application is always up, running, and ready to scale. With Kubernetes, you can automate many operational tasks, such as deployment, scaling, and updating your apps, thus increasing the reliability and 	availability of your applications.**

   	### Why Kubernetes?
  	- ***Scalability:*** Kubernetes makes scaling applications horizontally (adding more instances) easy.
	- ***Fault Tolerance:*** Ensures applications stay running even in case of node failures.
	- ***Service Discovery:*** Provides internal DNS and load balancing, allowing services to communicate seamlessly.
	- ***Rolling Updates & Rollbacks:*** You can roll out updates to applications incrementally and revert changes if needed.
   	### To Deploy Application on Kubernetes -> Create Kubernetes manifests
  	-  ***Namespace***:way to organize and divide Kubernetes resources (like Pods, Services, etc.) within the same cluster. They allow you to segment a cluster into different environments, teams, or projects while ensuring 		resource isolation and management.
   	 - ***Deployment***:Kubernetes object used to manage a set of identical Pods (running containers). It abstracts the complexity of updating, scaling, and rolling back applications.
  	-  ***Service***:  Kubernetes is an abstraction that defines how to access a group of Pods, either within the cluster or from the outside. It's essential for enabling communication between different components.
	-  ***Ingress***: Kubernetes resource that manages external access to services within a cluster, typically HTTP/HTTPS traffic. It provides a way to define rules for routing external traffic to the correct service based on hostnames or paths.
 	-  ***Limit Range***:  resource that helps to control the amount of CPU, memory, and storage that can be requested or consumed by containers or Pods.

    	## Helm
    	![helm-k8s](https://github.com/user-attachments/assets/16125732-d3f1-4001-a66a-e1ce5f3d4bd7)

    	Helm is a package manager for Kubernetes that simplifies the deployment of applications by allowing you to define, install, and upgrade even the most complex Kubernetes applications using charts (preconfigured Kubernetes resources bundled into a single package).
    	### Why Helm?
	- ***Efficiency:*** Helm allows you to deploy complex applications with a single command, automating Kubernetes resource management.
	- ***Versioning and Rollback:*** Helm manages versions of your deployed applications, making it easy to roll back to previous versions if necessary.
	- ***Reusability:*** Helm charts can be reused for multiple deployments, saving time and reducing error.
	- ***Easy Configuration:*** Customizable configurations make it easy to adjust Helm charts for different environments without modifying the core resources.

   	## Monitoring
	Monitoring is essential to ensure the health, performance, and reliability of applications and infrastructure. Monitoring systems help detect issues like slow response times, service downtime, or resource bottlenecks early, preventing larger failures and improving overall system stability.

	#### Prometheus
	![prometheus](https://github.com/user-attachments/assets/bb1f2348-7bfd-4aab-9d31-0815a443c2f0)
	**Prometheus** is a powerful open-source monitoring and alerting toolkit, designed to scrape metrics from services at specified intervals, store them, and alert based on predefined conditions.
	#### Grafana
	![grafana](https://github.com/user-attachments/assets/28fd6451-d5f6-4fdd-94cd-9cb63ff9d1b6)
	**Grafana** is an open-source platform used for monitoring and observability. It provides visualizations and dashboards for the metrics collected by Prometheus, allowing users to track system performance.
	#### Loki & Promtail
	![loki](https://github.com/user-attachments/assets/a844ba04-2b25-4203-8ded-41f4735953f6)
	- **Loki** is a log aggregation system designed to work closely with Prometheus and Grafana. It collects and stores logs from various sources, helping you debug issues by correlating logs with metrics.
	- **Promtail** is an agent that collects logs from applications and forwards them to Loki. It works similarly to Prometheus, but for log data
  
	### You Must make Configuration Files to Congifure the Monitoring tools
	- prometheus.yml for Prometheus.
	- loki-config.yaml for Loki.
	- promtail-config.yaml for Promtail.
	### To run the Monitoring stack, you'll use a Docker Compose file
	YAML file to configure and launch all the necessary containers for Prometheus, Grafana, Loki, and Promtail.

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
  	#You must be inside Terraform Folder
   
 ### Step 11: Ansible Installation
	sudo apt-get update
	sudo apt-get install ansible-core 

 ### Step 12: Run Ansible Playbook
	ansible-playbook -i inventory playbook.yml
  	#You must be inside Ansible Folder
   
 ### Step 13: Kubernetes Installation and Setup (Minikube)
 	curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
	sudo install minikube-linux-amd64 /usr/local/bin/minikube
 
 ### Step 14: Start Minikube
	minikube start
 
 ### Step 15: Apply Kubernetes Manifests:
 	kubectl apply -f namespace.yaml
  	kubectl apply -f deployment.yaml
	kubectl apply -f service.yaml
 	kubectl apply -f ingress.yaml
  	#You must be inside K8 Folder
   
 ### Step 16: Access the Application through Minikube
	#To get the minikube ip and port
	minikube service app-service -n app-namespace --url
	#or 
 	kubectl port-forward -n app-namespace svc/service port:targetport
  	#or
   	kubectl get nodes -o wide #to get ip
    	kubectl get all -n app-namespace #to get port
     
  ### Step 17 (optional): Expose Using Ingress (if necessary)
	minikube addons enable ingress
 
  ### Step 18: Install & Initialize Helm
 	curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
  	helm init

  ### Step 19: Create & install a Helm Chart (for your app)
	helm create your-app
	helm install your-release ./library-app #to install or upgrade an existing release(optional if there isany changes)
	helm rollback library-release 1 #Roll Back to a Previous Release(optional if i want to return to previous version)
 	#You must be inside Helm Folder
  
  ### Step 20: Run Docker Compose For Monitoring Stack 
  	docker-compose up -d #You must be inside Monitoring Folder

 
 > **Notes:**
 - > My DockerHub repo : https://hub.docker.com/repository/docker/mosami77/libimg
 - > Docker installation Resource : https://docs.docker.com/
 - > Terraform installtion Resource : https://developer.hashicorp.com/terraform/docs
 - > Ansible installation Resource : https://docs.ansible.com/
 - > Kuberenetes installation Resource : https://kubernetes.io/docs/
 - > Helm installation Resource : https://helm.sh/docs/
 - > Grafana Configuration Resource : https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/
 - > Prometheus Configuration Resource : https://prometheus.io/docs/prometheus/latest/configuration/configuration/
 - > Loki Configuration Resource : https://grafana.com/docs/loki/latest/configure/
 - > Promtail Configuration Resource : https://grafana.com/docs/loki/latest/send-data/promtail/configuration/
     
