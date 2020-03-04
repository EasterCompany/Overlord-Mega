<h1>THE FLASK/REACT OVERHAUL PROJECT</h1>
<h2> https://www.easter.company/ </h2>
<h5> 0. header </h5>
<h5> 1. installation </h5>
<h5> 2. usage </h5>
<h5> 3. flask backend tutorial </h5>
<h5> 4. react frontend tutorial </h5>
<br>
<h2> HEADER </h2>
<br> live build hosted on: 
<br> &nbsp;&nbsp;&nbsp;&nbsp; https://www.easter.company/
<br> beta build hosted on: 
<br> &nbsp;&nbsp;&nbsp;&nbsp; currently offline, sorry!
<br>
<h2> INSTALLATION </h2> 
<br> >> cd react-apps
<br> >> npm install
<br> >> npm run build
<br>
<h2> USAGE </h2>
<br> >> python main.py debug
<br>
<h4> readme.md & .gitignore </h4>
git repository assets will be removed if server is run in production mode
<br> "tmp" folder in the root directory is ignored and used by Easter Company Master Server
<br>
<br>
<h2> FLASK BACK END DOCUMENTATION </h2>
<h4> what's documented here? </h4>
./<br>
flaskApps/<br>
&nbsp;&nbsp;&nbsp;&nbsp;__init__.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;index.py<br>
templates/<br>
&nbsp;&nbsp;&nbsp;&nbsp;index.html<br>
static/<br>
main.py<br>
passenger_wsgi.py<br>
<br>
<b>flaskApps</b> - for Python Code<br>
<b>templates</b> - for HTML / CSS / JavaScript templates<br>
<b>static</b> - for static web objects & images<br>
<h4>passenger_wsgi.py</h4>
our passenger_wsgi is for our easter.company web server to recognise<br>
and set the root directory, this will also automatically detect our flask app and run it.<br>
<h4>main.py</h4>
Core functionality is too create our flask app and import all of our flask apps into one place.<br>
This also contains a function called _lib_fetch and we've wrote a script here that access the current<br>
python interperter and uses pip (if it is installed) to install & upgrade any python dependecies<br>
that our project requires - currently modules are manually listed but fucntionality for automatic<br>
detection is intended.<br>
<h4>__init__.py</h4>
declares that this folder contains python code / makes this directory a project module<br>
<h4>index.py</h4>
contains all of our app routes and web "map".<br>
routes "/" to the homepage for example<br>
or "/sign-up" to the sign-up page.<br>
<br>
<br>
<h2> REACT FRONT END DOCUMENTATION </h2>
<h4> CONNECTING /w FLASK </h4>
To connect our flask and react (front and backend) we can start by creating our react app template with<br>
&nbsp;&nbsp;&nbsp;&nbsp;>> create-react-app react-apps <br>
<br>
firstly we need to get access to our config and build by using:<br>
&nbsp;&nbsp;&nbsp;&nbsp;>> npm run eject 
<br>
<h5>CONFIG/PATH.JS</h5>
&nbsp;&nbsp;&nbsp;&nbsp;inside of our react-apps folder: open "config/path.js" and find<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;module.exports = { <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;appBuild: resolveApp('...') <br>
&nbsp;&nbsp;&nbsp;&nbsp;} 
<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;and update that to this:
<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;module.exports = { <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;appBuild: resolveApp('../static/react') <br>
&nbsp;&nbsp;&nbsp;&nbsp;} 
<br>
<h5>WEBPACK.CONFIG.JS</h5>
&nbsp;&nbsp;&nbsp;&nbsp;then in "webpack.config.js" we refractored all references to the static directory out of the file.
<br>
&nbsp;&nbsp;&nbsp;&nbsp;(ie; 'static/js' -> 'js')
<br>
<h5>CLASS: HtmlWebPackPlugin</h5>
&nbsp;&nbsp;&nbsp;&nbsp;lastly; inside of the HtmlWebpackPlugin class, right after:<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; { inject: true, <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; template: paths.appHtml, <br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;add: <br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; filename: "../../templates/index.html", }
<br>
<h5>PACKAGE.JSON</h5>
&nbsp;&nbsp;&nbsp;&nbsp;add: <br>
&nbsp;&nbsp;&nbsp;&nbsp;{ "homepage": "/static/react", } <br>
&nbsp;&nbsp;&nbsp;&nbsp;to the package.json 
<br>
<h4> Building our React </h4>
&nbsp;&nbsp;&nbsp;&nbsp;build our react app with <br>
&nbsp;&nbsp;&nbsp;&nbsp;>> npm run build <br>
<br> 
<b> enjoy very much success! </b> 
<br>
<b> more documentation can found on the website <b>
