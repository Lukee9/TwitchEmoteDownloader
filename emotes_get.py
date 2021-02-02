import os
import sys
import requests
import argparse

parser = argparse.ArgumentParser(description='Download HD Twitch emotes.')
parser.add_argument('--out', type=str, required=True, help='(Required) Path to output directory.')
parser.add_argument('-cs', '--case', action='store_true', help='Set if emote names are case sensitive. In which case the first matching result is chosen after sorting by usage count (descending).')
parser.add_argument('-q', '--quiet', action='store_true', help='Set to remove console output.')
parser.add_argument('--emotes', type=str, nargs='+', required=True, help='(Required) List of emote names, separated by a space.')
args = parser.parse_args()

if not os.path.isdir(args.out):
    print("ERROR: Output directory not found.")
    sys.exit(1)

api = 'https://api.frankerfacez.com/v1/emoticons'

for emote in args.emotes:
    if not args.quiet:
        print("Trying to grab %s" % emote)
    response = requests.get(api,
                            params={'q': emote,
                                    'sort': 'count-desc'})
    results = response.json()
    emote_name = emote if args.case else emote.upper()
    found = False
    for result in results['emoticons']:
        result_name = result['name'] if args.case else result['name'].upper()
        if emote_name == result_name:
            found = True
            # Grab highest definition and save it
            emote_url = list(result['urls'].values())[-1].lstrip('//')  # Last is highest definition
            emote_data = requests.get("https://%s" % emote_url)
            if emote_data.status_code == 200:
                write_path = os.path.join(args.out, "%s.png" % emote)
                open(write_path, 'wb').write(emote_data.content)
                if not args.quiet:
                    print("Successfully grabbed emote %s. Written to %s." % (emote, write_path))
            elif not args.quiet:
                print("ERROR: Failed to grab emote %s. Please try again." % emote)
            break
    if not args.quiet and not found:
        print("WARNING: Couldn't find emote with name %s" % emote)

