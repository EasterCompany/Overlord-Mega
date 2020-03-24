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
    var post_data = [];
    
    for (var p=0;p<my_data.length-1;p++) {
        post_data.push(
            [
                my_data[p].split(" ")[0],
                my_data[p].split(" ")[1],
                my_data[p].split(" ")[2]
            ]
        );
    }
    
    for (p=0;p<post_data.length;p++) {
        const post_signature = React.createElement('p', {}, post_data[p][1]);
        const post_content = React.createElement('p', {}, post_data[p][2]);
        posts.push(post_signature);
        posts.push(post_content);
    }
}


console.log(catchPostData());
serviceWorker.unregister();
