import React from 'react';
import { Link } from 'react-router-dom';
import * as bs from 'react-bootstrap';

import { IProject } from '../../common/types';

export interface IProjectListProps {
    projects: IProject[];
    handleProjectDeleteOnClick: (identifier: string) => void;
}

export function ProjectList({ projects, handleProjectDeleteOnClick }: IProjectListProps): JSX.Element {
    const cards = projects.map((row) => {
        return (
            <bs.Col key={ row.id }>
            <bs.Card className="project p-3 m-3">
                <bs.Card.Body>
                <bs.Card.Title style={{ position: "relative", textAlign: "center" }}>
                    <Link to={ `/projects/${row.id}/` }>{ row.name }</Link>
                    <em className="delete-project" title="Delete Project" onClick={ () => handleProjectDeleteOnClick(row.id) }>
                        <i className="bi bi-x"></i>
                    </em>
                </bs.Card.Title>
                </bs.Card.Body>
            </bs.Card>
            </bs.Col>
        );
    });

  return (
    <>
        {cards}
    </>
  );
}
