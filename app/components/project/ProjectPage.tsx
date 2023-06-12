import _ from 'lodash';
import React from 'react';
import { useParams } from 'react-router-dom';

export function ProjectPage(): JSX.Element {
    const { projectId } = useParams();

    return (
        <div>
            hi, {projectId}
        </div>
    );
}
