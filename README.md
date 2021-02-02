# Twitch Emote Downloader

A simple python3 script for easily downloading Twitch emotes from FrankerFaceZ.
Helpful for downloading emotes to add to your discord server.

### Note
This script selects the first emote which matches the given name after sorting the emotes into descending order of usage count to differentiate between emotes which have the same name. (i.e. it selects the most used emote with the given name).

### Dependencies
- Python3
- requests package:
	- `python -m pip install requests`

### Arguments
| Argument   | Description                                                                                                                         | Usage                       |
|------------|-------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| -\-out      | (Required) Path to output directory.                                                                                                | -\-out OUT                   |
| -cs -\-case | Set if emote names are case sensitive. In which case the first matching result is chosen after sorting by usage count (descending). | -cs                         |
| -q -\-quiet | Set to remove console output.                                                                                                       | -q                          |
| -\-emotes   | (Required) List of emote names, separated by a space.                                                                               | -\-emotes EMOTE [EMOTES ...] |


### Example Usage

    python3 emotes_get.py --out C:\Emotes -cs --emotes POGGERS FeelsGoodMan

### Known Issues

 - This script attempts to download the highest quality image for each emote however in cases where the lower quality version has been used more (i.e. higher usage count), the lower quality version will be downloaded instead.
 Example:
For emote 'POGGERS', an HTTP GET request is sent to:
https://api.frankerfacez.com/v1/emoticons?q=POGGERS&sort=count-desc
From that, the first matching emote, with ID 214129, (as of 02/02/2021) has 84992 uses. The highest quality image for this emote is: https://cdn.frankerfacez.com/emote/214129/1
The second matching emote, with ID 259306, has 8097 uses. The highest quality image for this emote is: https://cdn.frankerfacez.com/emote/259306/4
The second matching emote is simply a higher quality version of the first matching one, however in this case the first one is selected for download.

### TODO

 - Add argument to allow BetterTTV emotes to be used instead once their API has been documented.
 - Add way to download global Twitch emotes (e.g. 'Kappa')
 - Add exception handling.
 - Fix issue where lower quality version of emote is sometimes downloaded instead of the higher quality version (see 'Known Issues' above)

