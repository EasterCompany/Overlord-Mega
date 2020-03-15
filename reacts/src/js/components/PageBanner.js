import React from 'react';
import '../../css/header.css';

function page_banner(){
    return (
        <div className="App-header">
            <div className="row">
                <div className="column">
                    <button className="App-banner-show"></button>
                </div>
                <div className="column">
                    <p className="App-banner-title"> easter company </p>
                </div>
            </div>
            <div className="App-banner">
                <button className="App-banner-button">
                    <p>home</p>
                </button>
                <button className="App-banner-button">
                    <p>documentation</p>
                </button>
            </div>
        </div>
    );
}

export default page_banner;
