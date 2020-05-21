<h2 class="redline" style="text-align:center;">FULLSTACK DOCUMENTATION</h2>
<h6 style="text-align:center;"> you can view this documentation @ <a href='https://www.easter.company/documentation'>easter.company</a> & <a href='https://github.com/EasterCompany/Overlord/blob/master/README.md'>github</a></h6>
<h3> Download </h3>
<p>
  To begin you'll need to either download or clone the Overlord Repository.<br>
  On the github.com repo you can download a .zip of the latest version or alternatively you can clone the repository using<br>git -> this way you can update your framework to a newer version easily at a later date.<br>
  To do that enter into your terminal interface:<br>
  <code>git clone https://github.com/EasterCompany/Overlord.git</code>
</p>
<h3> Make a New App </h3>
<p> 
  To create a new web-app<br>while inside of the overlord directory in your terminal<br>
  Enter:<br>
  <code>./e -m hello-world</code><br>
  Or:<br>
  <code>./e make-web-app hello-world</code><br>
  <br>
  Your new app-folder will exist within your <code>template/app</code> directory named "hello_world" or other wise named how you instructed.
  Your app folder will contain an index html document with the same name as your app;<br>it is important that it remains this way - the file should also contain some boiler plate to help you get started.<br>Also inside of your app folder you will have a "src"folder. This folder should contain a <code>root.py</code> file.<br> The root.py should also contain boiler plate to get you started.<br>
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
