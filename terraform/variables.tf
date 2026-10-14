variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Environment name (e.g., production, dev)"
  type        = string
  default     = "production"
}

variable "allowed_origins" {
  description = "List of allowed origins for CORS"
  type        = list(string)
  default     = [
    "https://amdinycloud.com",
    "https://dinycloud.com",
    "https://d26hfhtuphuoh3.cloudfront.net"
  ]
}