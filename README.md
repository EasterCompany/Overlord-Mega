# Easter Company Web-App

easter.company website source code (eLang Backend)

# Installation

To retrieve the Overlord Project Framework run this command within the directory you would like to create (and/or) host your project.

```bash
git clone http://github.com/EasterCompany/Overlord.git
```

If you would like to install the entire Overlord umbrella stack use command line argument '--recursive' as used below.
If you would like to use ssh then use the git repo link as used below as well.

```bash
git clone --recursive git@github.com:EasterCompany/Overlord.git
```

# Execute Code to Post

inside the root directory

```bash
/usr/bin/python3 server.py
```

# Host Flask Web Server

inside the root directory

```bash
/usr/bin/python3 server.py start
```

# Run eLang Python Unit Tests

inside the root directory

```bash
/usr/bin/python3 server.py debug
```

# Do Everything

- execute to post with error messages
- run eLang test suite
- start flask web server if all pass

```bash
/usr/bin/python3 server.py start debug
```

read the docs @ [easter.company](https://www.easter.company/)
