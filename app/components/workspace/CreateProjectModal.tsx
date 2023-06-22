import React, { useState } from 'react';

import { ICreateProjectArgs } from '../../common/types';

import {
  CreateProjectForm,
  DEFAULT_CREATE_PROJECT_VALUES
} from './CreateProjectForm';

import * as bs from 'react-bootstrap';

export interface ICreateProjectModelProps {
  handleSubmit: (project: ICreateProjectArgs) => Promise<void>;
}

export function CreateProjectModal({ handleSubmit }: ICreateProjectModelProps): JSX.Element {
  const [project, setProject] = useState<ICreateProjectArgs>({ ...DEFAULT_CREATE_PROJECT_VALUES });
  const [showCreateProject, setShowCreateProject] = useState(false);

  const handleShowModalOnClick = () => setShowCreateProject(true);
  const handleCloseModalOnClick = () => {
    setProject({ ...DEFAULT_CREATE_PROJECT_VALUES });
    setShowCreateProject(false);
  };

  const handleProjectNameChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setProject({
      ...project,
      name: event.target.value
    });
  };

  const handleCreateNewProjectOnClick = () => {
    if (project.name === '') {
      return;
    }

    handleSubmit(project).then(handleCloseModalOnClick);
  };

  return (
    <>
      <bs.Button style={{ "width": "100%" }} onClick={handleShowModalOnClick}>New Project</bs.Button>
      <bs.Modal show={showCreateProject} onHide={handleCloseModalOnClick}>
        <bs.Modal.Header closeButton>
          <bs.Modal.Title>New Project</bs.Modal.Title>
        </bs.Modal.Header>
        <bs.Modal.Body>
          <CreateProjectForm project={project} handleNameChange={handleProjectNameChange} />
        </bs.Modal.Body>
        <bs.Modal.Footer>
          <bs.Button variant="secondary" onClick={handleCloseModalOnClick}>Cancel</bs.Button>
          <bs.Button variant="primary" onClick={handleCreateNewProjectOnClick}>Create</bs.Button>
        </bs.Modal.Footer>
      </bs.Modal>
    </>
  );
}
