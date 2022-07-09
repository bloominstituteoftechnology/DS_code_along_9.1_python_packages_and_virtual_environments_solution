# Code-Along 9.1 - Python Packages and Virtual Environments (SOLUTION)

## Requirements

- Text Editor (Visual Studio Code)
- Local Python Installation (Anaconda)
- Pipenv (for Virtual Environments)
- Command Line Application (Terminal - MacOS, Git Bash - Windows)

Setup instructions for all of these tools can be found in the [Unit 3 Setup Instructions](https://github.com/bloominstituteoftechnology/DS-Unit-3-Setup) and **must** be completed before participating in this Code-Along. 

## Set Up

### 1. [Log in or sign up for a Spotify Developer Account.](https://developer.spotify.com/dashboard/)

Once you're logged in, navigate to the Dashboard and select "Create An App"

![Spotify Develoepr Dashboard](https://github.com/bloominstituteoftechnology/code_along_main/blob/main/DS_Core/Unit_3/Sprint_11/Code_Along_1/assets/spotify_dashboard.png)

Give your app a name, description, and agree to the Terms of Service and Branding Guidelines.

![Set up App Details and Agree to TOS](https://github.com/bloominstituteoftechnology/code_along_main/blob/main/DS_Core/Unit_3/Sprint_11/Code_Along_1/assets/create_an_app.png)

Once you've complete these steps you will be presented with two password-looking things called: 

- Client ID
- Client Secret

2. Add the API Keys to the project:

You will need to create a `.env` file in the outer folder of this repository and add the Client ID and Client Secret to that file in the following format: 

```
CLIENT_ID=1886d8afa9b48aa93282286d88bd7bb
CLIENT_SECRET=a337e9d2f7034923df9ccd319459750
```

Make sure that you close down your virtual environment, and command line application and then your command line application and virtual environment or else these API keys in order to register these API keys with the project.

3. Run the main file as a script:

`python top_50.py`