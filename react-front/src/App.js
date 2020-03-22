import React from 'react';
import './App.css';


function App() {
  return (
    <div className="App">

      <header className="App-header">
        <h1> >> Hello World! </h1>
        <h4> $ fmp.learning.hour || simple is better</h4>
      </header>
    
      <body className="App-body">
        <form action="/make/post" method="get">
          <textarea id="new_post" className="App-post" maxLength="280" placeholder="make a new hello world learning note!" name="new_post" autoFocus />
          <h5> sign your post </h5>
          <input id="new_post_signature" maxLength="34" placeholder="email@findmypast.com" name="new_post_signature" type="email" />
        </form>

        <div id="posts" className="App-body-posts">
          <div id="post1" className="post">
          </div>
          <div id="post2" className="post">
          </div>
          <div id="post3" className="post">
          </div>
          <div id="post4" className="post">
          </div>
          <div id="post5" className="post">
          </div>
          <div id="post6" className="post">
          </div>
        </div>

      </body>

      <footer className="App-foot">
        <a href="https://github.com/EasterCompany/easter.company"> view on github </a>
      </footer>
    
    </div>
  );
}


export default App;
