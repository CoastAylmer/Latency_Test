#!/usr/bin/env python3
import subprocess
import time
import os

# Paths and credentials
exampleFile = "/home/csubuntupc/Downloads/100mb-examplefile-com.txt"
destinationPath = "MAylmer@192.168.1.38:/Users/MAylmer/Documents/scp_results"
mykey = 'Fuecoco2024$'
outputFile = "scp_results.txt"

# Ensure the file exists
if not os.path.exists(exampleFile):
    print(f"Error: FILE NOT FOUND: {exampleFile}")
    exit(1)

# Loop for multiple transfers
for i in range(1, 11):
    try:
        print(f"Starting SCP transfer {i} of 10....")

        # Construct the SCP command with sshpass
        scp_command = ["sshpass", "-p", mykey, "scp", "-v", exampleFile, destinationPath]

        # Using script to capture the SCP output
        command = ["script", "-q", "-c", " ".join(scp_command), outputFile]

        # Run the command using subprocess.Popen
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1  # Line-buffered output
        )

        # Wait for the process to finish
        process.wait()

        # Open the output file and process the results
        with open(outputFile, "r") as f:
            for line in f:
                # Filter only lines that contain "Transferred" or "Bytes per second"
                if "Transferred:" in line or "Bytes per second" in line:
                    print(line.strip())  # Print the raw SCP output

                    # Extract and process the "Bytes per second" line
                    if "Bytes per second" in line:
                        # Extract sent bytes per second (the first number before 'received')
                        parts = line.split(',')
                        sent_bytes_per_second = parts[0].split()[3]  # "sent <bytes>"
                        sent_bytes_per_second = float(sent_bytes_per_second)
                        
                        # Convert bytes per second to MB/s
                        sent_mb_per_second = sent_bytes_per_second / 1048576  # 1 MB = 1048576 bytes
                        print(f"Transfer speed: {sent_mb_per_second:.2f} MB/s")

        if process.returncode == 0:
            print(f"SCP transfer {i} completed successfully!")
        else:
            print(f"SCP transfer {i} failed with return code {process.returncode}")

    except Exception as e:
        print(f"Unexpected error in SCP transfer {i}: {e}")

    time.sleep(0.5)  # Optional delay between transfers
