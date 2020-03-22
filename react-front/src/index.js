import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
ReactDOM.render(<App />, document.getElementById('root'));


async function catchPostData() {
    const response = await fetch("/api?q=hello_world&r=posts");
    var my_data  = await response.text();
    
    my_data = my_data.split("<br>");
    for (var post in my_data) {
        console.log(my_data[post]);
    
    }
}


catchPostData();
serviceWorker.unregister();
