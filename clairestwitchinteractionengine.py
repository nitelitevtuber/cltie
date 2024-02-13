from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.type import AuthScope
import customtkinter
import tkinter
import sv_ttk
sv_ttk.set_theme("dark")
def twitchlogin():
    

app = customtkinter.CTk()
app.title("Claire's Twitch Interaction Engine")

app.geometry("400x150")

button = customtkinter.CTkButton(app, text="Authenticate", command=)
button.grid(row=0, column=0, padx=20, pady=20)

app.mainloop()





#grabs deets for use later 
async def login_logic():
    #authenticatates silly goofy little api thingie with the user 
    twitch = await Twitch('o958o6q8up44t8d4xlkxfqxid4f5bi', 'b1iha1fx3awubleroyxsxnslid6b4y')

    target_scope = [AuthScope.CHANNEL_MANAGE_REDEMPTIONS]
    auth = UserAuthenticator(twitch, target_scope, force_verify=False)
    #opens up browser and does silly goofy authentication, then adds in users specific deets to allow actual use of twitches apis.
    token, refresh_token = await auth.authenticate()
    await twitch.set_user_authentication(token, target_scope, refresh_token)
























    










  
    


 
