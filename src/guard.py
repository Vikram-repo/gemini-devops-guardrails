try:
    with open("terraform/main.tf", "r") as file:
        terraform_code = file.read()
except FileNotFoundError:
    print("❌ Error: terraform/main.tf file not found!")
    sys.exit(1)