import React, { useRef } from 'react';
import { Link } from 'react-router-dom';

import image from '../../images/label-baby.png';

export function Header(): JSX.Element {
    const header = useRef(null);
    return (
        <header ref={header}>
            <nav className='navbar navbar-expand-lg'>
                <Link to="/" className='navbar-brand'>
                    <img className='logo' src={ image } />
                </Link>
                <h1 className="title">Label Baby Jr.</h1>
            </nav>
        </header>
    );
}
