project               = "pro"
service_account_email = "sa@pro.iam.gserviceaccount.com"
gcp_user              = "user"

world_reachable_protocol_port_map = {
  "tcp" = "22,3306"
}

configuration = [
  {
    name  = "wg-medium"
    count = 4
    labels = {
      "role" = ["workload-generator"]
    }
    machine_type = "e2-standard-4"
    image        = "ubuntu-minimal-2004-focal-v20230427"
    tags = ["wg", "allow-internal"]
  },

  {
    name  = "mysql"
    count = 1,
    labels = {
      "role" = ["mysql"]
    }
    machine_type = "e2-standard-8"
    image        = "ubuntu-minimal-2004-focal-v20230427"
    tags = ["mysql", "allow-internal"]
    disk = {
      size = 100,
      type = "pd-ssd",
      name = "mysql-disk"
    }
  }
]
