from typing import OrderedDict
import gi, json
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf, Gdk

# Load CSS
css = ''
css_provider = Gtk.CssProvider()
css_provider.load_from_data(css)
context = Gtk.StyleContext()
screen = Gdk.Screen.get_default()
context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="About this PC")

        # Add a custom headerbar
        self.hb = Gtk.HeaderBar()
        self.hb.props.show_close_button = True
        self.set_titlebar(self.hb)

        # Add a stack and stack switcher
        self.stack = Gtk.Stack()
        self.add(self.stack)
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.stack.set_transition_duration(500)

        self.stack_sw = Gtk.StackSwitcher()
        self.stack_sw.set_stack(self.stack)
        self.hb.set_custom_title(self.stack_sw)

        # Initialize the "Overview" tab
        self.overview_init()
        
        # Initialize the "Displays" tab
        self.display_init()
        # Initialize the "Storage" tab
        self.storage_init()
        # Initialize the "Support" tab
        self.support_init()
        # Initialize the "Service" tab
        self.service_init()

    def overview_init(self):
        # Load information from json
        with open("overview-info.json", mode="rt") as f:
            conf = json.loads(f.read())

        # Horizontal box (2 col: distro image and info)
        overview_layout = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=conf["logo_space"])
        self.stack.add_titled(overview_layout, "overview_layout", "Overview")

        # Vert box (3 rows: distro_info, system_info, addi_btn)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=conf["section_space"])
        
        distro_info =  Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        system_info = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        addi_btn = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        # Set alignments
        distro_info.props.halign = system_info.props.halign = addi_btn.props.halign = Gtk.Align.START

        # Initialize distro info
        distro_name = Gtk.Label()
        distro_name.set_markup(conf["distro_markup"])
        distro_name.props.halign = Gtk.Align.START

        distro_ver = Gtk.Label(label=conf["distro_ver"])
        distro_ver.props.halign = Gtk.Align.START

        distro_info.pack_start(distro_name, False, False, 0)
        distro_info.pack_start(distro_ver, False, False, 0)

        # Initialize system info
        FIELD_SP = 20
        hostname = Gtk.Label(label=conf["hostname"])
        hostname.props.halign = Gtk.Align.START
        system_info.pack_start(hostname, False, False, 0)

        info_dict = {"Processor": conf["cpu"], "Memory": conf["memory"], "Startup Disk": conf["startup_disk"], "Graphics": conf["graphics"], "Serial Number": conf["serial_num"]}
        for key in info_dict:
            line = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=FIELD_SP)

            property_name = Gtk.Label()
            property_name.set_markup(f"<span font_weight='bold'>{key}</span>")
            property_name.props.halign = Gtk.Align.START

            line.pack_start(property_name, False, False, 0)
            line.pack_start(Gtk.Label(label=info_dict[key]), False, False, 0)
            line.props.halign = Gtk.Align.START
            system_info.pack_start(line, False, False, 0)
        
        # Initialize additional buttons
        sys_report_btn = Gtk.Button(label="System Report...")
        software_upd_btn = Gtk.Button(label="Software Update...")
        addi_btn.pack_start(sys_report_btn, False, False, 0)
        addi_btn.pack_start(software_upd_btn, False, False, 0)

        # Pack distro_info, system_info, addi_btn into vbox
        vbox.pack_start(distro_info, True, True, 0)
        vbox.pack_start(system_info, True, True, 0)
        vbox.pack_start(addi_btn, True, True, 0)

        # Intialize distro image
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            filename=conf["distro_image_path"], 
            width=conf["distro_image_size"][0], 
            height=conf["distro_image_size"][1], 
            preserve_aspect_ratio=True)

        distro_img = Gtk.Image.new_from_pixbuf(pixbuf)

        overview_layout.pack_start(distro_img, True, True, 0)
        overview_layout.pack_start(vbox, True, True, 0)

        overview_layout.props.margin_start = conf["overview_margins"][0]
        overview_layout.props.margin_end = conf["overview_margins"][1]
        overview_layout.props.margin_top = conf["overview_margins"][2]
        overview_layout.props.margin_bottom = conf["overview_margins"][3]
    
    def display_init(self):
        display_layout = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        display_layout.pack_start(Gtk.Label(label="Under development"), True, True, 0)
        self.stack.add_titled(display_layout, "display_layout", "Display")
    def support_init(self):
        support_layout = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        support_layout.pack_start(Gtk.Label(label="Under development"), True, True, 0)
        self.stack.add_titled(support_layout, "support_layout", "Support")
    def storage_init(self):
        storage_layout = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        storage_layout.pack_start(Gtk.Label(label="Under development"), True, True, 0)
        self.stack.add_titled(storage_layout, "storage_layout", "Storage")
    def service_init(self):
        service_layout = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        service_layout.pack_start(Gtk.Label(label="Under development"), True, True, 0)
        self.stack.add_titled(service_layout, "service_layout", "Service")


w = MainWindow()
w.connect("destroy", Gtk.main_quit)
w.show_all()
Gtk.main()
