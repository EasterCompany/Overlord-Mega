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
    var posts = [];
    for (var p=0;p<my_data.length-1;p++) {
        posts.push(
            [
                my_data[p].split(" ")[0],
                my_data[p].split(" ")[1],
                my_data[p].split(" ")[2]
            ]
        );
    }
    for (p=0;p<posts.length;p++) {
        console.log(posts[p]);
    }
}


catchPostData();
serviceWorker.unregister();
