# FILE-INTEGRITY-CHECKER

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: KEERTHANA SASIKUMAR

*INTERN ID*: CT04DF1796

*DOMAIN*: CYBER SECURITY AND ETHICAL HACKING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

It can be used as a file watcher:
File Watcher is a lightweight Python script that monitors a specified folder for any file changes, including additions, deletions, or modifications. It uses SHA-256 hashing to detect even the slightest change in file content and reports it in real time (on an interval basis);like for example 10 seconds
It:
->Monitors a given directory 
->Detects and logs:
1) New files
2) Deleted files
->Stores file hashes between runs in a JSON file (file_hashes.json)

HOW IT WORKS:
->The script calculates SHA-256 hashes of files in the watch directory.
->It compares the current snapshot with the previous one.
->Any detected changes are printed to the console.
->It runs continuously, checking for changes at a set interval (default: 10 seconds).

SAMPLE OUTPUT:
Monitoring directory: ./watch_folder

[NO CHANGES]

[CHANGE DETECTED]
  Added:
    + test1.txt

[CHANGE DETECTED]
  Removed:
    - test1.txt

Thus this script is ideal for detecting file tampering, configuration drift, or monitoring development folders....

#OUTPUT
![Image](https://github.com/user-attachments/assets/bfb644a8-131b-4469-91b1-ad8bb7997ca8)

![Image](https://github.com/user-attachments/assets/10c2e87d-349b-4da9-853a-36f40c865dd1)

![Image](https://github.com/user-attachments/assets/e4d6e44b-eca5-4ff4-aaad-5dbf2cb312a4)









