// IMPORT PROJECT
import React from 'react';

// IMPORT PAGE OBJECTS
import './App.css';
import Hero from './object/hero';


// PAGE APP FUNCTION (CLASS)
function App() {
  return (
    <div className="App">
      
      <header className="header">
        <Hero />
      </header>
      
      <body className="body">
      </body>
      
      <footer className="footer">
        <a className="App-link"
            href="http://github.com/eastercompany/easter.company"
            target="_blank"
            rel="noopener noreferrer"
          > view source
        </a>
      </footer>
    
    </div>
  );
}

export default App;
