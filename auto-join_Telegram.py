# make sure to have telethon and python-dotenv installed
# put API_ID and  API_HASH
# https://my.telegram.org/ for API


from telethon.sync import TelegramClient
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors.rpcerrorlist import FloodWaitError

import os
import asyncio

import pandas as pd
import numpy as np

API_ID = ""
API_HASH = ""

df = pd.read_csv('list_telegram.md',sep="|", header=0, skipinitialspace=True).dropna(
    axis=1, how="all"
).iloc[1:]

df['hash'] = np.where(df['Telegram'].str.contains('https://t.me/\+'), df['Telegram'].str.replace("https://t.me/+", ""), "")
df['username'] = np.where(df['hash']=="", df['Telegram'].str.replace("https://t.me/", ""), "")
df['Category'].fillna(df['Telegram'], inplace=True)

df = df.loc[(df['Registered'].isna()) & (df['Status'] == "ONLINE")]

async def main():
    with open("result.txt", "w") as txt_file:
        async with TelegramClient('tg_session', API_ID, API_HASH) as client:
            for ind in df.index:
                print("Joining : " + df['Category'][ind] + " " + str(ind) + "/" + str(len(df)))
                try:
                    if(df['hash'][ind] != ""):
                        await client(ImportChatInviteRequest(hash=df['hash'][ind]))
                    else:
                        await client(JoinChannelRequest(channel=df['username'][ind]))
                    print("Successfuly joined :" + df['Category'][ind])
                    txt_file.write(df['Category'][ind] + " : " + "OK" + "\n")
                    df['Registered'][ind] = "X"
                except FloodWaitError as fwe:
                    print(f'Waiting for {fwe}')
                    df['Registered'][ind] = "DEAD"
                    await asyncio.sleep(delay=fwe.seconds)
                except Exception as err:
                    txt_file.write(df['Category'][ind] + " - " + f"Encountered an error while joining {df['Category'][ind]} : {err}" + "\n")
                    df['Registered'][ind] = "DEAD"
                    print(f"Encountered an error while joining {df['Category'][ind]}\n{err}")
                


asyncio.run(main())