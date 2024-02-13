from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.type import AuthScope
import customtkinter
import tkinter

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


authwindow = customtkinter.CTk()
authwindow.title("Claire's Twitch Interaction Engine")
authwindow.geometry("1920x1028")
authwindow._state_before_windows_set_titlebar_color = 'zoomed'

button = customtkinter.CTkButton(authwindow, text="my button",)
button.grid(row=0, column=0, padx=890, pady=550, sticky="ew", columnspan=2)
label = customtkinter.CTkLabel(authwindow, text="Please authenticate with Twitch to continue.", fg_color="transparent", font=("Segoe UI Bold", 50))
label.grid(row=0, column=0, padx=930, pady=(0, 200), sticky="ew", columnspan=1)
authwindow.mainloop()

