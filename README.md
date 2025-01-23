SCP Transfer Script

Overview

This Python script automates the process of transferring files between devices using the scp command. Designed for network performance testing, it captures transfer statistics, calculates transfer speeds, and logs the results for easy sharing and analysis.

Usage

Run the script:

python3 scp_transfer.py

Follow the prompts:

Enter the path of the file to transfer.

Enter the destination in the format user@host:/path/to/destination.

Enter the SSH password if required.

The script will:

Validate inputs.

Perform SCP transfers (default: 10 iterations).

Log the results in transfer_summary.txt.

Output

The script generates two files:

scp_results.txt: Contains the raw output of the scp -v command for debugging purposes.

transfer_summary.txt: A clean and formatted summary of each transfer, including:

Bytes transferred

Transfer time

Transfer speed (MB/s)

Success or failure status

Example Output in transfer_summary.txt:

Starting SCP transfer 1 of 10....
Transferred: sent 104924004, received 18312 bytes, in 50.0 seconds
Bytes per second: sent 2099832.5, received 366.5
Transfer speed: 2.00 MB/s
SCP transfer 1 completed successfully!

Starting SCP transfer 2 of 10....
Transferred: sent 104923984, received 18212 bytes, in 44.2 seconds
Bytes per second: sent 2374754.4, received 412.2
Transfer speed: 2.28 MB/s
SCP transfer 2 completed successfully!

Configuration

To customize the script:

Update the default values (e.g., number of transfers, output filenames).

Modify the SCP command as needed for your use case.

Troubleshooting

"FILE NOT FOUND" Error: Ensure the source file path is correct.

Invalid Destination Format: Ensure the destination is in the correct format (e.g., user@host:/path/to/destination).

Permission Denied: Verify SSH access and the password provided.

Contributing

Feel free to submit issues or pull requests to enhance the script's functionality.

 

