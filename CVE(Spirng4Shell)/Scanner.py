import subprocess
import time
import os

def run_script(parameter):
    script_path = os.path.join(os.path.dirname(__file__), 'spring4shell.py')
    #script_path = 'C:/Users/superuser/Downloads/CVE-2022-22965-main/spring4shell.py'
    command = f'python "{script_path}" "{parameter}"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def analyze_result(result):
    if 'successfully' in result.lower():
        return 'Injection Success Check PLZ'
    elif 'cannot set' in result.lower():
        return 'This is Safe'
    else:
        return 'Unkwon analyze'

def main():
    input_file_path = os.path.join(os.path.dirname(__file__), 'URL.txt')
    output_file_path = os.path.join(os.path.dirname(__file__), 'Result.txt')
    #input_file_path='C:/Users/superuser/Downloads/CVE-2022-22965-main/URL.txt'
    #output_file_path='C:/Users/superuser/Downloads/CVE-2022-22965-main/Result.txt'

    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        lines = input_file.read().splitlines()

        for line in lines:
            output_file.write("----------\n")
            output_file.write(f"{line} 결과\n")
            print(f"Target: {line}")            
            output_file.write(f"{line}\n")
            result = run_script(line)
            summary = analyze_result(result)
            print(f"{result}\n")
            output_file.write(f"{result}\n") 
            print(f"this is {line} Result\n")
            output_file.write(f"{line} is {summary}\n")
            output_file.write("\n\n")

            print(f"Waiting for 1 sec before the next excution")
            time.sleep(10) #1min

if __name__ == "__main__":
    main()

