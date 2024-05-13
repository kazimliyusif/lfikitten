Automatic LFI and Path Traversal Scanner
This Python script is designed to automatically detect Local File Inclusion (LFI) and Path Traversal vulnerabilities in web applications.

Features
Automated Scanning: The script automates the process of scanning for LFI and Path Traversal vulnerabilities, saving time and effort.
Configurable Options: Users can configure various parameters such as the target URL, parameters, and verbose mode.

Easy to Use: Simple command-line interface makes it easy to run the scanner and interpret the results.
Usage
To use the scanner, follow these steps:

Installation: Clone the repository and navigate to the project directory.


Copy code
git clone https://github.com/kazimliyusif/lfikitten.git
cd lfikitten


Run the Scanner: Execute the main script with Python to learn about options.

python3 lfikitten.py --help


Requirements
Python 3.x

Example
Here's an example of how to run the scanner:

python3 lfikitten.py --url http://example.com -v -p 'page'
