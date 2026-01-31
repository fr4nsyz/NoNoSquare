import yaml

# cloud img
# users, packages
# runcmd
# ssh_pwauth
# disable_root: true


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"  # Resets the color/style


type BCOLOR = str


def print_pretty(s: str, color: BCOLOR):
    print(f"{color}{s}{bcolors.ENDC}")


def create_user_data(data):

    try:
        with open("user-data", "w") as f:
            user_data = f"""
                users:
                  {data["users"]["name"]}
                  {data["users"]["sudo"]}
                  {data["users"]["shell"]}
                  {data["users"]["ssh_authorized_keys"]}

                packages:
                  {"\n".join(f"- {x}" for x in data["packages"])}

                runcmd:
                  {"\n".join(f"- {x}" for x in data["runcmd"])}

                ssh_pwauth: {data["ssh_pwauth"]}
                disable_root: {data["disable_root"]}
                """
            f.write(user_data)
            print_pretty("[ CREATED ] user-data", bcolors.OKGREEN)


def main():

    file_path = "config.yaml"

    try:
        with open(file_path, "r") as file:
            data = yaml.safe_load(file)

        print("Data Loaded")

        print("Your config: ", data)

        create_user_data(data)

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except yaml.YAMLError as exc:
        print(f"Error parsing YAML file: {exc}")
