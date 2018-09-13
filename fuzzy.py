

from fuzzing.fuzzer import FuzzExecutor
file_list=["C:/Users/lxmi/OneDrive - Aarhus universitet/Sem 3/ISD/Morten/Documents/KL25P80M48SF0.pdf",
           "C:/Users/lxmi/OneDrive - Aarhus universitet/Sem 3/ISD/Morten/Documents/MCUXpresso_IDE_User_Guide(1).pdf"]

apps_under_test= ["C:/Program Files (x86)/Internet Explorer/iexplore.exe"]
number_of_runs= 13

def test():
    print("Start test")
    fuzz_executor= FuzzExecutor(apps_under_test, file_list)
    fuzz_executor.run_test(number_of_runs)
    print("Tests finished")
    return fuzz_executor.stats
def main():
    stats = test()
    print(stats)

if __name__=="__main__":
    main()
