#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Keyboard")

        self.board = Gtk.Grid()
        self.btn0 = Gtk.Button(label=" 0 ")
        self.btn1 = Gtk.Button(label=" 1 ")
        self.btn2 = Gtk.Button(label=" 2 ")
        self.btn3 = Gtk.Button(label=" 3 ")
        self.btn4 = Gtk.Button(label=" 4 ")
        self.btn5 = Gtk.Button(label=" 5 ")
        self.btn6 = Gtk.Button(label=" 6 ")
        self.btn7 = Gtk.Button(label=" 7 ")
        self.btn8 = Gtk.Button(label=" 8 ")
        self.btn9 = Gtk.Button(label=" 9 ")

                 #.attach(object, col, row, col_span, row_span)
        self.board.attach(self.btn1, 0, 0,1, 1 )
        self.board.attach(self.btn2, 1,0,1,1 )
        self.board.attach(self.btn3, 2,0,1,1 )
        self.board.attach(self.btn4, 0, 1,1, 1 )
        self.board.attach(self.btn5, 1, 1,1, 1 )
        self.board.attach(self.btn6, 2, 1,1, 1 )
        self.board.attach(self.btn7, 0, 2,1, 1 )
        self.board.attach(self.btn8, 1, 2,1, 1 )
        self.board.attach(self.btn9, 2, 2,1, 1 )
        self.board.attach(self.btn0, 0, 3,3, 1 )

        self.add(self.board)

win = MyWindow()
win.set_position = Gtk.WindowPosition.CENTER
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
