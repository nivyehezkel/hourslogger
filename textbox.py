#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Say something")
        self.set_size_request(1000, 700)
        # Spacing is in pixels
        self.box = Gtk.Box(orientation="vertical", spacing=2)
        self.add(self.box)
        self.btn = Gtk.Button(label="Speak")
        self.btn.connect("clicked", self.btn_clicked)
        self.ent = Gtk.Entry()
        self.ent.set_text("What do you want to say?")

        self.box.pack_start(self.btn, True, True, 0)
        self.box.pack_start(self.ent, True, True, 0)

    def btn_clicked(self, widget):
        print(self.ent.get_text())


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
