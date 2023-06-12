import _ from 'lodash';
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { ICreateProjectArgs, IProject } from '../../common/types';
import { WorkspaceService } from '../../services';
import { CreateProjectModal } from './CreateProjectModal';
import { Loading } from '../common';

import * as bs from 'react-bootstrap';

import '../../scss/workspace.scss';

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

  const handleDeleteProjectOnClickEvent = (identifier: string) => {
    setLoading(true);
    return workspaceService.delete(identifier).then(() => {
      setProjects(
        projects.filter((project: IProject) => project.id !== identifier)
      );
      
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

  if (_.isNil(projects)) {
    return (
        <Loading />
    );
  }

  const cards = projects.map((row) => {
    return (
      <bs.Col key={ row.id }>
        <bs.Card className="p-3 m-3">
          <bs.Card.Body>
            <bs.Card.Title style={{ position: "relative" }}>
              <Link to={ `/projects/${row.id}/` }>{ row.name }</Link>
              <em className="delete-project" onClick={ () => handleDeleteProjectOnClickEvent(row.id) }>
                <i className="bi bi-trash"></i>
              </em>
            </bs.Card.Title>
          </bs.Card.Body>
        </bs.Card>
      </bs.Col>
    );
  });

  return (
    <bs.Container>
      <bs.Row className="m-3">
        <bs.Col md={{ span: 6, offset: 3 }}>
          <CreateProjectModal
            handleSubmit={ handleCreateNewProjectOnClickEvent }
          />
        </bs.Col>
      </bs.Row>
      <bs.Row md={4}>
        { loading ? <Loading /> : cards }
      </bs.Row>
    </bs.Container>
  );
}
