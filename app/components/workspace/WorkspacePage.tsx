import _ from 'lodash';
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { ICreateProjectArgs, IProject } from '../../common/types';
import { WorkspaceService } from '../../services';
import { CreateProjectModal } from './CreateProjectModal';

import * as bs from 'react-bootstrap';

const workspaceService = new WorkspaceService();

function sort(projects: IProject[]): IProject[] {
  return _.orderBy(projects, (item) => item.name.toLowerCase(), 'asc');
}

export function WorkspacePage(): JSX.Element {
  const [loading, setLoading] = useState<boolean>(false);
  const [projects, setProjects] = useState<IProject[]>([]);

  const handleCreateNewProjectOnClickEvent = (args: ICreateProjectArgs): Promise<void> => {
    setLoading(true);
    return workspaceService.create(args).then((project) => {
      setProjects(sort([...projects, project]));
      setLoading(false);
    });
  };

  useEffect(() => {
    if (loading) {
        return;
    }

    setLoading(true);
    workspaceService.getAll().then((response) => {
      setProjects(sort(response));
      setLoading(false);
    });
  }, []);

  const cards = projects.map((row) => {
    return (
      <bs.Col key={ row.id }>
        <bs.Card className="p-3 m-3">
          <bs.Card.Body>
            <bs.Card.Title>
              <Link to={ `/projects/${row.id}/` }>{ row.name }</Link>
            </bs.Card.Title>
          </bs.Card.Body>
        </bs.Card>
      </bs.Col>
    );
  });

  return (
    <bs.Container>
      <bs.Row md={4}>
        { cards }
      </bs.Row>
      <bs.Row className="m-3">
        <bs.Col md={{ span: 6, offset: 3 }}>
          <CreateProjectModal handleSubmit={ handleCreateNewProjectOnClickEvent } />
        </bs.Col>
      </bs.Row>
    </bs.Container>
  );
}
