from spark_python_demo import EstimatePi, HudiGettingStarted

def main():
    # spark smoke test - is the basic spark env configured right
    # TODO: put proper tests in :)
    EstimatePi.go()
    # check out hudi
    HudiGettingStarted.go()

if __name__ == "__main__":
    main()