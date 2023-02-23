# Mastocli - Mastodon Timeline Reader

Mastocli is a command-line based timeline reader for Mastodon, built using Python. It allows you to view your Mastodon timeline, including your home timeline, local timeline, and federated timeline, all from the comfort of your terminal.
Installation

To install Mastocli, simply clone the repository to your local machine, and install the required dependencies using pip.


```
$ git clone https://github.com/mac-lawson/mastocli.git
$ cd mastocli
$ pip install Mastodon.py
$ pip install curses
$ pip install colorama
```

Usage

Before using Mastocli, you will need to provide your Mastodon email and password. To do so, open the default.py file located in the Mastocli folder, and change the following lines:

```

email = ""
password = ""
```
Replace the empty strings with your Mastodon email and password, and save the file.

Once you have provided your Mastodon credentials, you can use Mastocli to view your Mastodon timeline. To do so, simply run the following command:


```
$ python3 visual.py
```