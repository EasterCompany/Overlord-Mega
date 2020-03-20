import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
ReactDOM.render(<App />, document.getElementById('root'));

const posts = () => { 
    var posts = null;
    fetch('/api?q=hello_world&r=posts')
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        posts = data;
    });
    return posts;
}
document.getElementById("posts").innerText = posts

serviceWorker.unregister();
