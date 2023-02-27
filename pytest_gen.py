import yaml

def init_configuration(fname='init.yaml') -> {}:
    configuration = {
        "input_test": "input.txt",
        "results": "output.txt",
        "method": "func"
    }
    try:
        with open(fname, "w") as f:
            yaml.dump(configuration, f)
    except:
        return None
    finally:
        return configuration


def get_configuration(fname='init.yaml') -> {}:
    configuration = {}
    try:
        with open(fname, "r") as f:
            configuration = yaml.load(f, Loader=yaml.FullLoader)
            return configuration
    except:
        return None


class StepikTestGenerator:
    __stream_input_test = None
    __stream_results = None

    # читаем из файлов
    def __init__(self, fname_input_test, fname_results, method):
        with open(fname_input_test, 'r') as f:
            self.__stream_input_test = f.readlines()

        with open(fname_results, 'r') as f:
            self.__stream_results = f.readlines()
        self.__method = method

    # читаем из файлов изначально через объект настроек
    def __init__(self, configuration):
        fname_input_test = configuration.get("input_test")
        fname_results = configuration.get("results")
        method = configuration.get("method")
        self.__init__(fname_input_test, fname_results, method)

    # читаем из потоков (строк)
    def __init__(self, stream_input_test, stream_results, method):
        self.__stream_input_test = stream_input_test
        self.__stream_results = stream_results
        self.__method = method


    def doit(self):
        pass










