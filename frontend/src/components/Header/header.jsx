import React from 'react';
import './header.css';
// Import an image for logo here

const Header = () =>(
    <div className=''>
        <div className='header-content'>
            <h1 className=''>Amharic Text to Speech Data Collection Platform</h1>
            <h1 className=''>የአማርኛ ንግግርን መሰብሰቢያ ገፅ</h1>

            <p>This is a Data collection platform that will be used to prepare text-to-speech corpuses for the Amharic language!!!</p>
            <p>ይህ የመረጃ መሰብሰቢያ ገፅ ነው:: የአማርኛ ቋንቋን ከጽሑፍ ወደ ንግግር ቀይሮ ለማዘጋጀት ይጠቅማል!!!</p>
            <p>Here you can verify previously recorded audio or you can record a new one!!!</p>
            <p>እዚህ ቀደም የተቀዳውን ድምጽ ማረጋገጥ ይችላሉ ወይም አዲስ መቅዳት ይችላሉ !!!</p>
            <div className=''>
                <button type="button">Audit Previous Recordings</button>
            </div>
        </div>
    </div>

);
export default Header;