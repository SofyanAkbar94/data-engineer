variable "project" {
  description = "Project"
  default     = "terraform-de-412207"
}

variable "region" {
  description = "Region"
  #Update the below to your desired region
  default     = "ASIA-SOUTHEAST2"
}

variable "location" {
  description = "Project Location"
  #Update the below to your desired location
  default     = "ASIA-SOUTHEAST2"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  #Update the below to what you want your dataset to be called
  default     = "de_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  #Update the below to a unique bucket name
  default     = "terraform-de-412207-terra-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}