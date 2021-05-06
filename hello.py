import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="main")
        self.btn = Gtk.Button(label="Add row")
        self.btn.connect("clicked", self.add_row)
        self.add(self.btn)
    def add_row(self, widget):
        print("Gtk is best")
    

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
