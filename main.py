from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.type import AuthScope
from twitchAPI.oauth import UserAuthenticationStorageHelper
from twitchAPI.helper import first
import customtkinter
import tkinter
import asyncio

# grabs deets for use later 
async def login_logic():
    # authenticates silly goofy little api thingie with the user
    twitch = await Twitch('o958o6q8up44t8d4xlkxfqxid4f5bi', 'b1iha1fx3awubleroyxsxnslid6b4y')
    
    target_scope = [AuthScope.CHANNEL_MANAGE_REDEMPTIONS]
    auth = UserAuthenticator(twitch, target_scope, force_verify=False)
    
    # opens up the browser and does silly goofy authentication,
    # then adds in the user's specific details to allow actual use of Twitch's APIs.
    token, refresh_token = await auth.authenticate()
    await twitch.set_user_authentication(token, target_scope, refresh_token)
    helper = UserAuthenticationStorageHelper(twitch, target_scope)
    await helper.bind()

def login_deez():
    asyncio.run(login_logic())


authwindow = customtkinter.CTk()
authwindow.title("Claire's Twitch Interaction Engine")
authwindow.geometry("1920x1028")
authwindow._state_before_windows_set_titlebar_color = 'zoomed'

#i know this code is spagetti, but it works, and thats all i care about 
button = customtkinter.CTkButton(authwindow, text="Authenticate ", command=login_deez)
button.grid(row=1, column=0, padx=0, pady=(0, 600))
label = customtkinter.CTkLabel(authwindow, text="Please authenticate with Twitch to continue.", fg_color="transparent", font=("Segoe UI Bold", 30),)
label.grid_columnconfigure(0, weight=1)
label.grid(row=0, column=0, padx=0, pady=(20, 0))
authwindow.grid_rowconfigure(0, weight=1)
authwindow.grid_rowconfigure(1, weight=1)
authwindow.grid_columnconfigure(0, weight=1)


authwindow.mainloop()



def mainwindow():
    mainwindow = customtkinter.CTk()
    mainwindow.title("Claire's Twitch Interaction Engine")
    mainwindow.geometry("1920x1028")
    mainwindow._state_before_windows_set_titlebar_color = 'zoomed'
