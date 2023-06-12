import React, { useRef } from 'react';
import { Link } from 'react-router-dom';

import image from '../../images/label-baby.png';

export function Header(): JSX.Element {
    const header = useRef(null);
    return (
        <header ref={header}>
            <nav className='navbar navbar-expand-lg'>
                <Link to="/" className='navbar-brand'>
                    <img src={ image } style={{ width: '75px', marginLeft: "25px" }} />
                </Link>
            </nav>
        </header>
    );
}
