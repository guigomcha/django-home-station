# Google Drive API 
Based on a credentials.json file, this module will allow the user to connect to their Google Drive account in order to 
download the images that will be displayed in the form of a digital photo frame.
 
## How to run
Since this API will access to the develper's google account, they will need to follow some initial steps outside the 
scope of this project.
1. Create a developer account under https://console.developers.google.com/
2. The process to create a project and enable the Google Drive API requires a number of steps. I recommend following 
this demo to familiarize to the workflow. https://codelabs.developers.google.com/codelabs/gsuite-apis-intro/#1
3. Download your OAuth 2.0 credentials, rename to credentials.json and place at the same level of utils.py
4. Run the test file and check the contents of the image.png file that should appear under the test folder.


## Troubleshoot
It is known that Google's Python libraries might behave differently based on the IDE used. It is recommended to have
your IDE of choice run with admin privileges to avoid such situation. If the errors persists, try the following:


```
cd google_drive_api
pip uninstall -r requirements.txt
python -m pip install -U --force-reinstall pip
pip install -U pip google-api-python-client oauth2client
```


