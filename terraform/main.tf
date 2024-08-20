terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  profile = "default" # the profile which be defualt at the top of secret access key 
  region  = var.region
}

resource "aws_instance" "my_ec2" {
  ami           = "ami-04a81a99f5ec58529" # Ubuntu 24.04 LTS (us-east-1)
  instance_type = "t2.micro"              # Change this to your desired instance type
  security_groups = ["${aws_security_group.allow_ssh.name}"] #to make the security group
  key_name =  "vockey"   #default key
  tags = {
    Name = "MyTerraformInstance"
  }
}

