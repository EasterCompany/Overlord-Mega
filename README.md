<h2 class="redline" style="text-align:center;">FULLSTACK DOCUMENTATION</h2>
<h6 style="text-align:center;"> you can view this documentation @ <a href='https://www.easter.company/documentation'>easter.company</a> & <a href='https://github.com/EasterCompany/Overlord/blob/master/README.md'>github</a></h6>
<h3> Download </h3>
<p>
  To begin you'll need to either download or clone the Overlord Repository.<br>
  On github.com you can download a .zip of the latest version of Overlord or alternatively you can clone the repository using<br>git from your terminal -> this way you can update your framework to a newer version easily at a later date.<br>
  To do that - enter the following into your terminal:<br>
  <code>git clone https://github.com/EasterCompany/Overlord.git</code>
</p>
<h3> Install </h3>
<p>
  You will need to enter the directory you just downloaded inside your terminal.<br>
  like so; <code> cd Overlord </code> <br>
  <br>
  To use the elang interface you will need to be inside of this directory and start any command line with <code> ./e </code> <br><br>
  The full overlord stack doesn't require many external dependencies and most should already be on your system -- however there is an installation process for redundency. This will check (and/or) acquire any external packages that may be required for your system including those that may need upgraded. To use this installation feature simply use the <code>install</code> argument with the elang interface.<br>
  The install argument can either be used two ways;<br>
  firstly <code> ./e install </code><br>
  secondly <code> ./e -i </code><br>
  There aren't many interace arguments and they can all be shortned down to "-" + the first characater of the argument.<br>
  Other need-to-know arugments are:<br>
  <code>server || -s</code> starts the elang server<br>
  <code>make-web-app || -m</code> makes an edoc app<br>
  <code>test || -t</code> runs & logs all testing envrionments<br>
  for example you could string all these together like this:<br>
  <code>./e -i -m new-app -t -s</code> to install any required dependencies, make a new app called 'new-app', run and log any local testing envrionments and then start the server.<br>
</p>
<h3> Make a New App </h3>
<p> 
  To create a new web-app<br>while inside of the overlord directory in your terminal<br>
  Enter:<br>
  <code>./e -m hello-world</code><br>
  Or:<br>
  <code>./e make-web-app hello-world</code><br>
  <br>
  Your new app-folder will exist within your <code>./template/app</code> directory named "hello_world" or other wise named how you instructed.
  Your app folder will contain an index html document with the same name as your app;<br>it is important that it remains this way - the file should also contain some boiler plate to help you get started.<br>Also inside of your app folder you will have a "src" folder. This folder should contain a <code>root.py</code> file which should also contain some boiler plate to help get you started.<br>
</p>
<h4> ELANG BACKEND </h4>
<p> 
  We can control our elang backend with Python within our "root.py" file.<br>
  <code>ETML</code> is our raw index html file for our app.<br>
  <code>FILE</code> is our read e-doc virtual file object.<br>
  for example we could add after that;<br>
  <pre>items = archive(<br>&nbsp;&nbsp;'inventory',<br>&nbsp;&nbsp;default_cols = [<br>&nbsp;&nbsp;&nbsp;&nbsp;('item', 'text'),<br>&nbsp;&nbsp;&nbsp;&nbsp;('quantity', 'int')<br>&nbsp;&nbsp;]<br>)</pre><br>
  and this will use elang.archive to make an automated backend database for a inventory <br>
  with "item", "quantity" -> "date_added", "date_modified" and "unique_id" as properities.<br>
</p>
<h4> EDOCS FRONTEND </h4>
<p> We can control our edocs frontend with ETML & JS within our "index html" file. </p>
