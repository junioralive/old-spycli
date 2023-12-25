<a name="readme-top"></a>
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/junioralive/spy-cli">
    <img src="https://github.com/junioralive/spy-cli/assets/54473944/463a6d6b-d24f-4d58-927a-7a40dbb12347" alt="Logo" width="80" height="80">
  </a>

  <p align="center">
    A cli tool to browse and watch Movies/Shows/MORE, mainly focused on Bollywood & Indian Entertainment (Hindi Audio). 
    <br />
    <br />
    <a href="https://github.com/junioralive/spy-cli/issues">Report Bug</a>
    ·
    <a href="https://github.com/junioralive/spy-cli/issues">Request Feature</a>
  </p>
</div>


<h1 align="center">
	Showcase
</h1>


https://github.com/junioralive/spy-cli/assets/54473944/1423f1a2-37b2-45be-88c6-4781220bf969


<!-- TABLE OF CONTENTS -->
### Table of Contents
<ol>
  <li>
    <a href="#about-the-project">About The Project</a>
  </li>
  <li>
    <a href="#getting-started">Getting Started</a>
    <ul>
      <li><a href="#prerequisites">Prerequisites</a></li>
      <li><a href="#installation">Installation</a></li>
      <ul>
        <li><a href="#windows">Windows</a></li>
        <li><a href="#linux">Linux</a></li>
        <li><a href="#mac">MAC</a></li>
        <li><a href="#android">Android</a></li>
        <li><a href="#ios">iOS</a></li>
      </ul>
    </ul>
  </li>
  <li><a href="#usage">Usage</a></li>
  <li><a href="#disclaimer">Disclaimer</a></li>
  <li><a href="#contributing">Contributing</a></li>
  <li><a href="#contact">Contact</a></li>
  <li><a href="#inspiration">inspiration</a></li>
</ol>


<!-- ABOUT THE PROJECT -->
## About The Project

SPY-CLI provides a command-line interface (CLI) tool named `spy-cli` that allows users to stream movies or TV shows directly from the command line. It is compatible with multiple platforms including Android, Windows, Linux, macOS, and iPhone. Mainly focused on Bollywood & Indian Entertainment (Hindi Audio).

Note: It requires a backend API, For API details, [spycli-api](https://github.com/junioralive/spycli-api).

No API No problem, READ about [spycli-noserver](https://github.com/junioralive/spycli-noserver) before using.

<p align="right">(<a href="#readme-top">back to top</a>)</p


<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

- [`MPV`](https://mpv.io) - player used for Windows, macOS, Linux and Android
- [`VLC`](https://apps.apple.com/us/app/vlc-media-player/id650377962) - player used for iOS


## Installation


<!-- WINDOWS -->
### Windows

  - Make sure [`Python`](https://www.python.org/) (pip)[https://pip.pypa.io/en/stable/installation/] and (git)[https://git-scm.com/downloads] are installed.
  - Run this Command inside your Terminal (Installing fzf):
    ``` 
    winget install fzf
    ```
  - Clone the repository:
    ``` 
    git clone https://github.com/junioralive/spy-cli.git
    ```
  - Navigate to the cloned directory:
    ``` 
    cd spy-cli
    ```
  - Installing setuptools:
    ``` 
    pip install --upgrade setuptools wheel
    ``` 
  - Install requirements and dependencies:
    ``` 
    pip install -e .
    ```
  - First time run:
    ``` 
    spy-cli.config
    ```
    
Enter your API URL, choose your platform and you're all set. For API details, [spycli-api](https://github.com/junioralive/spycli-api).
No API No problem, READ about [spycli-noserver](https://github.com/junioralive/spycli-noserver) before using.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LINUX -->
### Linux

  - Make sure `Python` (pip)[https://pip.pypa.io/en/stable/installation/] and (git)[https://git-scm.com/downloads] are installed.
  - Run this Command inside your Terminal (Installing fzf):
    ``` 
    sudo apt-get install fzf
    ```
  - Clone the repository:
    ``` 
    git clone https://github.com/junioralive/spy-cli.git
    ```
  - Navigate to the cloned directory:
    ``` 
    cd spy-cli
    ```
  - Installing setuptools:
    ``` 
    pip install --upgrade setuptools wheel
    ``` 
  - Install requirements and dependencies:
    ``` 
    pip install -e .
    ```
  - First time run:
    ``` 
    spy-cli.config
    ```
    
Enter your API URL, choose your platform and you're all set. For API details, [spycli-api](https://github.com/junioralive/spycli-api).
No API No problem, READ about [spycli-noserver](https://github.com/junioralive/spycli-noserver) before using.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MAC -->
### MAC

  - Make sure (Python)[https://www.python.org/] (pip)[https://pip.pypa.io/en/stable/installation/] and (git)[https://git-scm.com/downloads] are installed.
  - Open the Terminal application on your Mac (Installing Homebrew:
    ``` 
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
  - Installing fzf:
    ``` 
    brew install fzf
    ```
  - Clone the repository:
    ``` 
    git clone https://github.com/junioralive/spy-cli.git
    ```
  - Navigate to the cloned directory:
    ``` 
    cd spy-cli
    ```
  - Installing fzf:
    ``` 
    sudo apt-get install fzf
    ```
  - Installing setuptools:
    ``` 
    pip install --upgrade setuptools wheel
    ``` 
  - Install requirements and dependencies:
    ``` 
    pip install -e .
    ```
  - First time run:
    ``` 
    spy-cli.config
    ```
    
Enter your API URL, choose your platform and you're all set. For API details, [spycli-api](https://github.com/junioralive/spycli-api).
No API No problem, READ about [spycli-noserver](https://github.com/junioralive/spycli-noserver) before using.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ANDROID --> 
### Android            

  - Make sure [MPV](https://play.google.com/store/apps/details?id=is.xyz.mpv) and [Termux](https://play.google.com/store/apps/details?id=com.termux) are installed.
  - Run following commands (Note: this may take a while)
    ```
    pkg update && pkg upgrade
    pkg install python git fzf
    pip install wheel
    git clone https://github.com/junioralive/spy-cli.git
    cd spy-cli
    pip3 install -e .
    ```
  - First time run:
    ``` 
    spy-cli.config
    ```
Enter your API URL, choose your platform and you're all set. For API details, [spycli-api](https://github.com/junioralive/spycli-api).
No API No problem, READ about [spycli-noserver](https://github.com/junioralive/spycli-noserver) before using.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- IOS -->
### iOS

  - Make sure [VLC MEDIA PLAYER](https://apps.apple.com/us/app/vlc-media-player/id650377962) and [iSH](https://apps.apple.com/us/app/ish-shell/id1436902243) are installed.

  - Run following commands (Note: this may take a while)
    ```
    apk update && apk upgrade
    apk add python3 git fzf
    python3 -m ensurepip --upgrade
    git clone https://github.com/junioralive/spy-cli.git
    cd spy-cli
    pip3 install -e .
    ```
  - First time run:
    ``` 
    spy-cli.config
    ```
    
Enter your API URL, choose your platform and you're all set. For API details, [spycli-api](https://github.com/junioralive/spycli-api).
No API No problem, READ about [spycli-noserver](https://github.com/junioralive/spycli-noserver) before using.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

Type: ```spy-cli``` into your Commandline.

### For no-server version

Type: ```spy-cli-basic``` into your Commandline.

READ about [spycli-noserver](https://github.com/junioralive/spycli-noserver) before using.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- DISCLAIMER -->
## Disclaimer

This project is designed to be utilized at the discretion and responsibility of the user, taking into consideration the specific legal and governmental regulations applicable to their context. The project does not exercise control over the nature of the content it disseminates. Consequently, any use of copyrighted material sourced from providers falls under the user’s own risk and accountability, and is not the responsibility of the project developers

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- Feature -->
## Feature

If you want a feature, create an [issue](https://github.com/junioralive/spy-cli/issues/new) or create the feature and make a pull request.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Pull requests are welcome and _appreciated_. For major changes, please open an issue first to discuss what you would like to change.


<!-- CONTACT -->
## Contact

Author: JuniorAlive | ```Discord: junioralive```

Project Link: [https://github.com/junioralive/spy-cli](https://github.com/junioralive/spy-cli)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- Inspiration -->
## Inspiration

Heavily inspired from [ani-cli](https://github.com/pystardust/ani-cli) [mov-cli](https://github.com/pystardust/mov-cli)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
