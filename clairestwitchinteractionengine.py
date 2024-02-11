from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.type import AuthScope
import customtkinter
import tkinter
import asyncio

customtkinter.set_appearance_mode("dark")
mainwindow = customtkinter.CTk()
mainwindow.geometry("1920x1028")
mainwindow._state_before_windows_set_titlebar_color = 'zoomed'
mainwindow.title("Claire's Twitch Interaction Engine")


frame = customtkinter.CTkFrame(master=mainwindow, fg_color="transparent")
frame.pack(pady=120, padx=120)
frame.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=1, anchor="c")
authbutton = customtkinter.CTkButton(master=frame, text="Authenticate")
authbutton.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


mainwindow.mainloop()
#grabs deets for use later 
async def login_logic():
    #authenticatates silly goofy little api thingie with the user 
    twitch = await Twitch('o958o6q8up44t8d4xlkxfqxid4f5bi', 'b1iha1fx3awubleroyxsxnslid6b4y')

    target_scope = [AuthScope.CHANNEL_MANAGE_REDEMPTIONS]
    auth = UserAuthenticator(twitch, target_scope, force_verify=False)
    #opens up browser and does silly goofy authentication, then adds in users specific deets to allow actual use of twitches apis.
    token, refresh_token = await auth.authenticate()
    await twitch.set_user_authentication(token, target_scope, refresh_token)
























    










  
    


 
