from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.type import AuthScope
import customtkinter
import tkinter
import asyncio

#i stole this code from customtikiter example code, i was too lazy to go and make my own, its 11 at night. let me cook.
class Authenticatonwindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

        self.label = customtkinter.CTkLabel(self, text="ToplevelWindow")
        self.label.pack(padx=20, pady=20)


class mainwindow(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1920x1028")
        self.after(0, lambda:self.state('zoomed'))
        self.title("Claire's Twitch Interaction Engine")
        self.toplevel_window = Authenticatonwindow(self)


        self.toplevel_window = None



mainwindow = mainwindow()
mainwindow.mainloop()

#grabs deets for use later 
async def login_engine():
    #authenticatates silly goofy little api thingie with the user 
    twitch = await Twitch('o958o6q8up44t8d4xlkxfqxid4f5bi', 'b1iha1fx3awubleroyxsxnslid6b4y')

    target_scope = [AuthScope.CHANNEL_MANAGE_REDEMPTIONS]
    auth = UserAuthenticator(twitch, target_scope, force_verify=False)
    #opens up browser and does silly goofy authentication, then adds in users specific deets to allow actual use of twitches apis.
    token, refresh_token = await auth.authenticate()
    await twitch.set_user_authentication(token, target_scope, refresh_token)
























    










  
    


 
