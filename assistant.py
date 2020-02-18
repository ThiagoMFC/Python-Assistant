import wx
import wikipedia
import wolframalpha
from gtts import gTTS
import os


class MyFrame(wx.Frame):
    answer = ""

    def __init__(self):
        wx.Frame.__init__(self, None, pos=wx.DefaultPosition, size=wx.Size(450, 100),
                          style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX |
                                wx.CLIP_CHILDREN, title="Assistant")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel, label="Ask me anything")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(400, 30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        user_input = self.txt.GetValue()
        user_input = user_input.lower()
        try:
            # wolframalpha appID
            app_id = ""
            client = wolframalpha.Client(app_id)

            result = client.query(user_input)
            answer = next(result.results).text

            print(answer)
            speech = gTTS(text=answer, lang='en', slow=False)
            speech.save('answer.mp3')
            os.system("start answer.mp3")
        except:
            answer = wikipedia.summary(user_input)
            print(answer)
            speech = gTTS(text=answer, lang='en', slow=False)
            speech.save('answer.mp3')
            os.system("start answer.mp3")




if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()