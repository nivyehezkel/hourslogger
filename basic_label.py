#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="main")
        # Spacing is in pixels
        self.box = Gtk.Box(orientation="vertical", spacing=2)
        self.add(self.box)
        self.btn = Gtk.Button(label="Boo")
        self.btn.connect("clicked", self.btn_clicked)
        self.lbl = Gtk.Label("Where is everyone?")

        self.box.pack_start(self.btn, True, True, 0)
        self.box.pack_start(self.lbl, True, True, 0)

    def btn_clicked(self, widget):
        self.lbl.set_text("There you are!")


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
