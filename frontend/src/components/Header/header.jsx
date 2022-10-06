import React from 'react';
import './header.css';
// Import an image for logo here

const Header = () =>(
    <div className=''>
        <div className='header-content'>
            <h1 className=''>Amharic Text to Speech Data Collection Platform</h1>
            <p>This is a Data collection platform that will be used to prepare text-to-speech corpuses for the Amharic language!!!</p>
            <p>Here you can vertify previously recorded audio or you can record a new one!!!</p>
            <div className=''>
                <button type="button">Audit Previous Recordings</button>
            </div>
        </div>
    </div>

);
export default Header;