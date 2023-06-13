import _ from 'lodash';
import React from 'react';
import { useParams } from 'react-router-dom';

import * as bs from 'react-bootstrap';
import '../../scss/project.scss';

export function ProjectPage(): JSX.Element {
    const { projectId } = useParams();

    return (
        <bs.Container>
            hi, { projectId }
        </bs.Container>
    );
}
