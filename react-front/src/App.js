import React from "react";
import "./App.css";
import logo from "./resources/logo.jpg";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-header-logo" alt="easter company logo" />
        <h2 className="App-header-title">
          EasterCompany
          <br />
          open source technology
        </h2>
        <button className="App-header-tool-mobile" />
      </header>
      <body className="App-body">
        <form action="/api?q=hello_world&r=make_post" method="get">
          <input id="q" name="q" type="hidden" value="hello_world" />
          <input id="r" name="r" type="hidden" value="make_post" />
          <textarea
            id="new_post"
            className="App-post"
            maxLength="280"
            placeholder="make a post!"
            name="new_post"
            autoFocus
          />
          <h5> user </h5>
          <input
            id="user"
            maxLength="64"
            placeholder="me@easter.company"
            name="user"
            type="email"
          />
        </form>
        <div id="posts" className="App-body-posts"></div>
      </body>
      <footer className="App-foot">
        <a href="https://github.com/EasterCompany/easter.company">
          {" "}
          view on github{" "}
        </a>
      </footer>
    </div>
  );
}

export default App;
