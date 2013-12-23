#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import os


try:
    import pygtk
    pygtk.require("2.0")
except:
    pass
try:
    import gtk
    import gtk.glade
except:
    sys.exit(1)


#resim klası
class Resim:
    def __init__(self):
        self.gladefile = "tasarim.glade"
        self.wTree = gtk.glade.XML(self.gladefile)

        dic = {"on_button1_clicked": self.button1_clicked,
               "on_window1_destroy": gtk.main_quit, }
        self.wTree.signal_autoconnect(dic)
        self.label4 = self.wTree.get_widget("label4")
        self.entry2 = self.wTree.get_widget("entry2")
        self.entry3 = self.wTree.get_widget("entry3")
        self.filechooserbutton1 = self.wTree.get_widget("filechooserbutton1")
        self.label4.set_text("")

    def button1_clicked(self, widget):
        dizinadi = self.filechooserbutton1.get_filename()+"/"
        dizinadi = dizinadi.replace(" ", "\ ")
        resimeni = self.entry2.get_text()
        resimboyu = self.entry3.get_text()
        unlem = ""
        if resimeni != "" and resimboyu != "":
            unlem = "!"

        os.system(
            'mogrify -resize ' + resimeni + 'x' + resimboyu + unlem +
            ' ' + dizinadi + '*.jpg')
        os.system(
            'find ' + dizinadi +
            ' -name \'*.jpg \' | xargs mogrify -strip')
        self.label4.set_text("Tüm Resimler Boyutlandırıldı")


if __name__ == "__main__":
    uyg = Resim()
    gtk.main()
