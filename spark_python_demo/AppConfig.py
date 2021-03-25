import os


def _get_env(variable:str): 

    var = os.getenv(variable)

    if var:
      return var

    else:
        msg = f"Environment variable '{variable}' not found"

        raise Exception(msg)    


def get_environment():
    return _get_env("ENVIRONMENT")

def get_hudi_data_root():
    return _get_env("HUDI_DATAROOT")

def get_delta_data_root():
    return _get_env("DELTA_DATAROOT")

def get_log_level():
    return _get_env("LOG_LEVEL")


is_local_environment:bool = get_environment() == "local"