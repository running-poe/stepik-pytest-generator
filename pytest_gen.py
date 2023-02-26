import yaml

def init_configuration(fname='init.yaml') -> bool:
    configuration = {
        "input_data": "input.txt",
        "output_data": "output.txt",
        "method": "func"
    }

    with open(fname, "w") as f:
        yaml.dump(configuration, f)


def get_configuration(fname='init.yaml') -> {}:
    configuration = {}
    try:
        with open(fname, "r") as f:
            configuration = yaml.load(f, Loader=yaml.FullLoader)
    finally:
        return configuration


def parse_input(p_in: []) -> []:
    pass


def parse_input(fname: str) -> []:
    pass








