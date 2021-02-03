# About this fake Mac

The "About this Mac" that most macOS rices miss.

<center>
<img src="first-preview.png" style="max-height:100px;"/>
<img src="first-bigsur-preview.png" style="max-height:100px;"/>
</center>

# Introduction
- I love macOS, because it profits both advantages of Linux and Windows: a Unix shell, and the abundance of popular industry standard softwares (like Microsoft Office, Adobe *, ...). The most important thing is that its UI is soooo stunning!<br>
I had used it for about a year on a Hackintosh until upgraded to a more powerful machine, but it is powered by an AMD Ryzen CPU. So, no more Hackintosh. I found my way (back) to Arch Linux and KDE Plasma (actually I had used them prior to macOS) and did all the ricing stuff (you can find my setup [here](https://github.com/hungngocphat01/KDEintosh)). I realized that all macOS rices ever always miss one thing: the "About this Mac" window. That's why I created this - a simple GTK 3.0 application to mimic it.
- This software is still under development and not fully tested.
- You are allowed to freely copy, make changes and redistribute this script, as long as you credit me as the original author.

# Dependencies
- bash
- neofetch
- dmidecode

# Installing
- Get and apply a GTK macOS theme first. `WhiteSur-dark-gtk` is highly recommeded.
- Download the png file of your distro logo (transparent background recommended) and take note of its path because the program will require it later.
- Git clone this repo to somewhere.
    ```bash
    cd mcos-about
    cd src
    make install
    ```

# Running
- Run from the terminal:
    ```bash
    mcos-about
    ```
- You can read more options in the help document of the program:
    ```bash
    mcos-about help
    ```
- You can also run it without a terminal (suitable for something like Kpple Menu) by executing:
    ```bash
    mcos-about-noterm
    ```
- You can pass arguments to the `mcos-about-noterm` exactly like the regular `mcos-about`, but it will not output to any terminal.
- In case you ran the `noterm` version of the program and nothing happened, try to run the regular version to see errors output to the terminal if there are any.

# Configuration file
- Since generating the system info to mimic the macOS style requires root access, so I decided to generate and write the system info to a json file (first run only). Upon next launches, the script will read and display the system info stored in the mentioned file. As a consequence, you will have to re-configure the program each time you upgrade your hardware or your distro, or else the information will stay the same, but this process is not very time-consuming.
- The program allows you to freely create, load and manipulate the configuration files. You can edit your displayed system specifications to suit your needs.
- The configuration file is a json file, and it has the following properties:
    - `distro_image_path`: A string denoting the path of the distro image.
    - `distro_image_size`: A list, consists of the size of the given image (members must be numeric).
    - `distro_markup`: A pango markup string, denoting the format of the displayed distro name.
    - `distro_ver`: Clear enough.
    - `hostname`: Device name. It can be laptop models on laptops.
    - `cpu`: Clear enough.
    - `memory`: RAM.
    - `startup_disk`: The label or name of the device where `/` is mounted.
    - `graphics`: GPU name.
    - `serial_num`: Clear enough.
    - `overview_margins`: A list consist of 4 numbers respectively denotes the left, right, top and bottom margin of - the overview window (members must be numeric).
    - `section_space`: A numeric value speciying the gap between the distro name/ver section, the system info section and the two bottom buttons section.
    - `logo_space`: A numberic value repensenting the gap between the distro logo and the info column.
    - `system_info_command`: The command run when 'System Info' button is clicked (have not implemented).
    - `software_update_command`: The command run when 'Software Update' button is clicked (have not implemented).
    - `font-family`: The font family for the whole program. Must be null if not specified (default font will be used) (have not implemented).

- Sample config file 1:
    ```json
    {
    "distro_image_path": "/home/ngocphat/local/share/mcos-about/distro-logo.png",
    "distro_image_size": [
        160,
        160
    ],
    "distro_markup": "<span font-size='xx-large'><span font-weight='bold'>Arch Linux</span></span>",
    "distro_ver": "5.10.11-arch1-1",
    "hostname": "20UD0001CD ThinkPad T14 Gen 1",
    "cpu": "2.100GHz AMD Ryzen 5 PRO 4650U",
    "memory": "16.0 GB 3200 MHz DDR4",
    "startup_disk": "nvme0n1p1",
    "graphics": "AMD ATI 07:00.0 Renoir",
    "serial_num": "L1XXXXX02GE",
    "overview_margins": [
        60,
        60,
        60,
        60
    ],
    "section_space": 20,
    "logo_space": 60,
    "system_info_command": "",
    "software_update_command": "",
    "font-family": null
    }
    ```

- Sample config file 2 (for faking a MacBook on macOS rices):
    ```json
    {
    "distro_image_path": "/home/ngocphat/local/share/mcos-about/bigsur.png",
    "distro_image_size": [
        160,
        160
    ],
    "distro_markup": "<span font-size='xx-large'><span font-weight='bold'>macOS </span>Big Sur</span>",
    "distro_ver": "Version 11.0.1",
    "hostname": "MacBook Pro 2020 (Early, 13-inch)",
    "cpu": "2.100GHz AMD Ryzen 5 PRO 4650U",
    "memory": "16.0 GB 3200 MHz DDR4",
    "startup_disk": "Macintosh HD",
    "graphics": "AMD Radeon RX Vega 5 2 GB",
    "serial_num": "XXXXXXXXXXXXXX",
    "overview_margins": [
        60,
        60,
        60,
        60
    ],
    "section_space": 20,
    "logo_space": 60,
    "system_info_command": "",
    "software_update_command": "",
    "font-family": "San Francisco Display"
    }
    ```

# Roadmap
- Implement "Display" and "Storage" tab.

# Changelog
```
v0.2 (04/02/2021)
- System information generation done.

v0.1 (02/02/2021)
- Initial build.
```
