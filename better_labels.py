#!/usr/bin/env python3


import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Better Labels")

        self.box = Gtk.Box(orientation="vertical", spacing=2)
        self.add(self.box)
        self.evbox = Gtk.EventBox()
        self.evbox.override_background_color(0, Gdk.RGBA(0.8, 0, 0, 1))

        self.lbl1 = Gtk.Label("Some")
        self.lbl2 = Gtk.Label("Stuff")

        self.evbox.add(self.lbl1)

        self.box.pack_start(self.evbox, True, True, 0)
        self.box.pack_start(self.lbl2, True, True, 0)



win = MyWindow()
win.set_position = Gtk.WindowPosition.CENTER
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
