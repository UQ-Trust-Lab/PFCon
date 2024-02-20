# PFCon
This is the code repo of PFCon

## Folder structure
```
├── README.md
├── INSTALL.md
├── GPT4_c.py
│
├── authorization
│	├── auto_connect_services.py
│	├── pre_process_service.py
│	├── tools.py
├── dataset
│	├── channel_info_cleaned.txt
│	├── applets_info_60000.txt
│


```

## authorization:
run `auto_connect_services.py` to authenticate and authorize the connection between services and IFTTT.

## dataset:
it contains all functionality artifacts fetched from the homepage of IFTTT, including both service-level and applet-level, please refer to our paper for more details.

## Usage
The file GPT4_c.py provides several examples of how to assign tasks to  ChatGPT. You need to specify your open API key in the code. Then, you can obtain the task result of the original sentence.

## Prompt
Our paper provides a detailed demonstration of the CoT and tutorials of prompts for different tasks.
