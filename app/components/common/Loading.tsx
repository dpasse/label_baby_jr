import React from 'react';
import ClipLoader from 'react-spinners/ClipLoader';

export function Loading(): JSX.Element {
    return (
        <ClipLoader
            className='loader'
            loading={true}
            cssOverride={{ display: 'block', margin: 'auto' }}
        />
    )
}
