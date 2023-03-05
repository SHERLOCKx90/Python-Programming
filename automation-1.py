from pywinauto.application import Application
app = Application(backend="uia").start("MicrosoftTeams.exe")
"""app.UntitledNotepad.menu_select("File->SaveAs")
app.SaveAs.ComboBox5.select("UTF-8")
app.SaveAs.edit1.set_text("Example-utf8.txt")
app.SaveAs.Save.click()"""
