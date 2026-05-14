# Placeholder variables
variable "region" {
  type    = string
  default = "us-east-1"
}

variable "name_prefix" {
  type    = string
  default = "churn"
}

# GitHub settings (for CodePipeline Source stage)
variable "github_owner" {
  type        = string
  description = "GitHub username/org that owns the repo"
}

variable "github_repo" {
  type        = string
  description = "GitHub repository name"
}

variable "github_oauth_token" {
  type        = string
  description = "GitHub OAuth token (use Terraform variables/TF Cloud/Secrets manager in real setups)"
  sensitive   = true
}


