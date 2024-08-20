

variable "container_port" {
  description = "Internal port the container listens on"
  type        = number
  default     = 80
}

variable "host_port" {
  description = "Host port to map to the container port"
  type        = number
  default     = 8080
}
variable "region" {
  type    = string
  default = "us-east-1"
}




