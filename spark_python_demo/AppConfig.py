import os
# from .SparkContext import log


def _get_env(variable:str): 

    var = os.getenv(variable)

    if var:
      return var

    else:
        msg = f"Environment variable '{variable}' not found"
        # log.error(msg)

        raise Exception(msg)    


def get_environment():
    return _get_env("ENVIRONMENT")


def get_data_root():
    return _get_env("ENVIRONMENT")

def get_log_level():
    return _get_env("LOG_LEVEL")


is_local_environment:bool = get_environment() == "local"