import gi
import pandas as pd

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# Path to the CSV file
hours_db = pd.DataFrame()
csv_path = ''
class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()

    def load_csv(self, button):
        global csv_path, hours_db
        hours_db = pd.read_csv(csv_path)

    def file_changed(self, button):
        global csv_path
        csv_path = button.get_filename()



builder = Gtk.Builder()
builder.add_from_file("hourslogger.glade")
print(type(builder.get_object('office_combo')))
combo_yn= builder.get_object('office_combo')
combo_yn.append_text("Yes")
combo_yn.append_text("No")
builder.connect_signals(Handler())

window = builder.get_object("HoursLogger")
window.show_all()

Gtk.main()
