<!--
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

# KaamelottBot Autoresponder

<p align="center">
 
  <!-- logo of the project here -->
  <img height="300" src="https://i.imgflip.com/3rc97h.png" alt="logo"/>  
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

- [KaamelottBot Autoresponder](#kaamelottbot-autoresponder)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Presentation](#presentation)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Release History](#release-history)
  - [Contributing](#contributing)
  - [License](#license)

<!-- Introduction -->
## Introduction
This project is a bot discord based on the universe of kaamelott.
Discord is a VoIP, instant messaging and digital distribution platform. (https://en.wikipedia.org/wiki/Discord_(software)) and Kaamelott is a French comedy medieval fantasy television series created, directed, written, scored, and edited by Alexandre Astier. (https://en.wikipedia.org/wiki/Kaamelott)

## Presentation

KaamelottBot Autoresponder is a discord bot coded in python with the discord.py library. It uses the spacy library, the 'fr_core_news_lg' pack, and the scripts of the first episodes of kaamelotts to determine the answer that is the most appropriate. Moreover he can also realize simple discord commands

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Resynchronize the package index files 
```sh
sudo apt-get update
```
install python 3.8

```sh
sudo apt install python3.8
```
install the python libraries

```sh
pip install discord
pip install spacy
pip install nltk
```

download the spacy french language pack
```sh
python3 -m spacy download fr_core_news_lg
```

### Installation

1. Clone the repo
```sh
git clone https://github.com/louispr81/KaamelottAutoResponder
cd KaamelottAutoResponder
```
In the folder KaamelottAutoResponder create a file "private.py". Write your bot token in this file like this (how to get a discord bot token : https://www.writebots.com/discord-bot-token/) :
```python
token="[Insert yout bot token here]"
```

Launch bot.py

Congratulations the bot is now active !
Invite him to your discord server (https://discordjs.guide/preparations/adding-your-bot-to-servers.html#bot-invite-links)

<!-- RELEASE HISTORY--> 
## Release History 

* <a href="https://github.com/louispr81/KaamelottAutoResponder/releases/tag/1.0">1.0</a>
    * Simple command executions (help, start, stop,...)
    * The bot responds with the answer that it thinks is the most appropriate
    * Choice of character 


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, 
inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the *license* License. See [LICENSE](license-url) for more information.

<!-- MARKDOWN LINKS & IMAGES -->

[contributors-shield]: https://img.shields.io/github/contributors/louispr81/KaamelottAutoResponder.svg?style=flat-square
[contributors-url]: https://github.com/louispr81/KaamelottAutoResponder/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/louispr81/KaamelottAutoResponder.svg?style=flat-square
[forks-url]: https://github.com/louispr81/KaamelottAutoResponder/network/members

[stars-shield]: https://img.shields.io/github/stars/louispr81/KaamelottAutoResponder.svg?style=flat-square
[stars-url]: https://github.com/louispr81/KaamelottAutoResponder/stargazers

[issues-shield]: https://img.shields.io/github/issues/louispr81/KaamelottAutoResponder.svg?style=flat-square
[issues-url]: https://github.com/louispr81/KaamelottAutoResponder/issues

[license-shield]: https://img.shields.io/github/license/louispr81/KaamelottAutoResponder.svg?style=flat-square
[license-url]: https://github.com/louispr81/KaamelottAutoResponder/blob/[branch]/LICENSE

[cpp-ver-shield]: https://img.shields.io/badge/C%2B%2B-11-blue.svg
[cpp-ver]: https://en.wikipedia.org/wiki/C%2B%2B11

[build-status-shield]: https://github.com/louispr81/KaamelottAutoResponder/workflows/CI/badge.svg
[build-status]: https://github.com/louispr81/KaamelottAutoResponder/actions

[version-shield]: https://img.shields.io/badge/version-0.0-blue.svg?cacheSeconds=2592000