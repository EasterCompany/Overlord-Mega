<h2 class="redline"> OVERLORD FULLSTACK WEB FRAMEWORK DOCUMENTATION </h2>
<h3> Download </h3>
<p>
  To begin you'll need to either download or clone the Overlord Repository.<br>
  On the github.com repo you can download a .zip of the latest version or alternatively you can clone the repository using<br>"git" -> this way you can update your framework to a newer version easily at a later date.<br>
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
  Your new (app / page) will exist within your <code>template/app</code> directory with named "hello_world".<br>
  Your app folder will contain an index html document with the same name as your app; it is important that it remains this<br>way - it should contain some boiler plate to help you get started. Inside of your app folder you will have a "src"<br>folder. This folder should contain a <code>root.py</code> file.<br>
  The root.py will also contain boiler plate to get you started.<br>
</p>
<h4> ELANG BACKEND </h4>
<p> 
  We can control our elang backend with Python within our "root.py" file.<br>
  <code>ETML</code> is our raw index html file for our app.<br>
  <code>FILE</code> is our read e-doc virtual file object.<br>
  for example we could add after that;<br>
  <pre>items = archive(\n
    'inventory',\n
    default_cols = [</br>
      ('item', 'text'),</br> 
      ('quantity', 'int')<br> 
    ]\n
  )</pre>
  <br>
  and this will use elang.archive to make an automated backend database for a inventory <br>
  with "item", "quantity" -> "date_added", "date_modified" and "unique_id" as properities.<br>
</p>
<h4> EDOCS FRONTEND </h4>
<p> We can control our edocs frontend with ETML & JS within our "index html" file. </p>
