#!/usr/bin/env python3
import subprocess
import time
import os
import re


def validate_file_path(file_path):
    if not os.path.exists(file_path):
        print(f"Error: FILE NOT FOUND: {file_path}")
        return False
    return True


def validate_destination(destination):
    # Regular expression to match the pattern user@host:/path
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+:.+$"
    if not re.match(pattern, destination):
        print(f"Error: Invalid destination format: {destination}")
        return False
    return True


while True:
    exampleFile = input("Enter the path of the file to transfer: ")
    if validate_file_path(exampleFile):
        break

while True:
    destinationPath = input("Enter the destination (e.g., user@host:/path): ")
    if validate_destination(destinationPath):
        break


mykey = input("Enter your password for SSH (if needed): ")


outputFile = input("Enter the path for the output file (default: scp_results.txt): ").strip()
if not outputFile:
    outputFile = "scp_results.txt"


with open(outputFile, "w") as f:
    f.write("SCP Transfer Results:\n\n")


for i in range(1, 11):
    try:
        
        transfer_info = f"Starting SCP transfer {i} of 10....\n"
        
        # Construct the SCP command with sshpass
        scp_command = ["sshpass", "-p", mykey, "scp", "-v", exampleFile, destinationPath]

        # Run the command using subprocess.Popen
        process = subprocess.Popen(
            scp_command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1  
        )

        
        stdout, stderr = process.communicate()

       
        transferred = None
        bytes_per_second = None
        for line in stderr.splitlines():
            if "Transferred:" in line:
                transferred = line.strip()
            elif "Bytes per second" in line:
                bytes_per_second = line.strip()

        
        if transferred and bytes_per_second:
            transfer_info += transferred + "\n"
            transfer_info += bytes_per_second + "\n"

            # Calculate transfer speed in MB/s
            match = re.search(r"sent (\d+)", bytes_per_second)
            if match:
                bytes_per_second_sent = float(match.group(1)) # Get the 'sent' bytes per second 
                transfer_speed_MB = bytes_per_second_sent / (1024 * 1024)  # Convert bytes to MB
                transfer_info += f"Transfer speed: {transfer_speed_MB:.2f} MB/s\n"
            
            # Append the transfer info with success message
            transfer_info += f"SCP transfer {i} completed successfully!\n"
        else:
            transfer_info += f"Error: Transfer {i} failed to retrieve data.\n"

        # Append the transfer information to the summary file
        with open(outputFile, "a") as result_file:
            result_file.write(transfer_info + "\n")  # Add a newline between transfers

        
        print(transfer_info)

    except Exception as e:
        print(f"Unexpected error in SCP transfer {i}: {e}")

    time.sleep(0.5)  

print("\nTransfer results have been saved to scp_results.txt.")