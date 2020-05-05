# Easter Company Overlord Full Stack Web-App

easter.company website source code (eLang Backend)

## Installation

To retrieve the Overlord Project Framework run this command within the directory you would like to create (and/or) host your project.

```bash
git clone http://github.com/EasterCompany/Overlord.git
```

If you would like to install the entire Overlord umbrella stack use command line argument '--recursive' as used below.
If you would like to use ssh then use the git repo link as used below as well.

```bash
git clone --recursive git@github.com:EasterCompany/Overlord.git
```

### Execute Code to Post

inside the root directory

```bash
/usr/bin/python3 server.py
```

### Host Flask Web Server

inside the root directory

```bash
/usr/bin/python3 server.py start
```

### Run eLang Python Unit Tests

inside the root directory

```bash
/usr/bin/python3 server.py debug
```

### Do Everything

- execute to post with error messages
- run eLang test suite
- start flask web server if all pass

```bash
/usr/bin/python3 server.py start debug
```

read the docs @ [easter.company](https://www.easter.company/)

## DOCUMENTATION SYSNOPSIS

### modules

#### elang

is a python library used for speeding up development, maximizing code-reuse and extensibility while keeping maintanence requirements to a minimum.

#### database

contains .py files with sql objects that can be used to create sets of tables within the local database and should be included within the server.py specification.

#### services

contains python micro-service api programs to be called on the host machine by other platforms or users to send and request information.

### public

contains miscellaneous files that contain site-reader information.

### static

#### build

contains built eDoc files that are ready for distribution

#### icon

contains various icon image files such as favicons, bookmark images and thumbnails.

#### image

contains various static image files

### templates

#### pages

contains a directory map of the site
