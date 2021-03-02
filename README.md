# MUDAE STATS

## Installation

First of all, you need to install [DiscordChatExporter](https://github.com/Tyrrrz/DiscordChatExporter).

To do so, either follow the [link](https://github.com/Tyrrrz/DiscordChatExporter/wiki) or use Docker in CLI.

Here's the command using Docker if you use a Bot Token:

```
docker run --rm -v -it /path/on/machine:/app/out:z tyrrrz:discordchatexporter:stable -export -t TOKEN -b -c CHANNELID -o data -f json
```

Replace TOKEN by your Bot Token and CHANNELID by the channel id.


If you are using your own token, be careful as that breaks discord's ToS and use the following command:

```
docker run --rm -v -it /path/on/machine:/app/out:z tyrrrz:discordchatexporter:stable -export -t TOKEN -c CHANNELID -o data -f json
```
Once again, replace TOKEN by your token and CHANNELID by the channel id.


## How to use the python script

Simply run the following command:

```
python3 mudae_occurence.py
```
