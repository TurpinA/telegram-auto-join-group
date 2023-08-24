# telegram-auto-join-group
This script autojoin a list of groups links from a markdown file

Add your API ID and HASH in the script

links can be invitation links or links with username in it.

|Telegram|Status|Category|Registered |
| ------ | ------ | ------ | ------ |
|https://t.me/+XXXXXXXX|ONLINE|Category1|
|https://t.me/+XXXXX|ONLINE|Category1|X|
|https://t.me/username2|ONLINE|Category1|DEAD|
|https://t.me/username|ONLINE|Category1|
|https://t.me/username677|OFFLINE|Category1|

Category is used for logging during the execution
Registered is used to mark as :
- X all group that are alaready joined, so don't need to join again.
- DEAD all dead links
