import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
ReactDOM.render(<App />, document.getElementById('root'));


async function catchPostData() {
    const post_data = [];
    const api_data  = await fetch("/api?q=hello_world&r=posts");

    for (let p=0;p<api_data.length-1;p++) {
        post_data.push(
            [
                api_data[p].split(" ")[0],
                api_data[p].split(" ")[1],
                api_data[p].split(" ")[2]
            ]
        );
    }    
    
    const posts = [];
    
    for (let p=0;p<post_data.length;p++) {
        const post_signature = React.createElement('p', {}, post_data[p][1]);
        const post_content = React.createElement('p', {}, post_data[p][2]);
        posts.push(post_signature);
        posts.push(post_content);
    }
    return posts
}


console.log(catchPostData());
serviceWorker.unregister();
