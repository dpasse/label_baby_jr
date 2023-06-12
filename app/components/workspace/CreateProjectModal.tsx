import React, { useState } from 'react';

import { ICreateProjectArgs } from '../../common/types';

import * as bs from 'react-bootstrap';

export interface ICreateProjectProps {
  handleSubmit: (project: ICreateProjectArgs) => Promise<void>;
}

export function CreateProjectModal({ handleSubmit }: ICreateProjectProps): JSX.Element {
  const [state, setState] = useState<string>('');
  const [showCreateProject, setShowCreateProject] = useState(false);

  const handleNewProjectOnClick = () => setShowCreateProject(true);
  const handleCloseNewProjectOnClick = () => {
    setShowCreateProject(false);
    setState('');
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setState(e.target.value);
  }

  const handleCreateNewProjectOnClick = () => {
    if (state === '') {
      return;
    }

    const project: ICreateProjectArgs = {
      name: state,
    };

    handleSubmit(project).then(() => {
      setShowCreateProject(false);
      setState('');
    });
  };

  return (
    <>
      <bs.Button style={{ "width": "100%" }} onClick={handleNewProjectOnClick}>New Project</bs.Button>
      <bs.Modal show={showCreateProject} onHide={handleCloseNewProjectOnClick}>
        <bs.Modal.Header closeButton>
          <bs.Modal.Title>New Project</bs.Modal.Title>
        </bs.Modal.Header>
        <bs.Modal.Body>
          <bs.Form.Label htmlFor="project-name">Name:</bs.Form.Label>
          <bs.Form.Control id="project-name" type="text" onChange={ handleChange } value={ state }/>
        </bs.Modal.Body>
        <bs.Modal.Footer>
          <bs.Button variant="secondary" onClick={handleCloseNewProjectOnClick}>Cancel</bs.Button>
          <bs.Button variant="primary" onClick={handleCreateNewProjectOnClick}>Create</bs.Button>
        </bs.Modal.Footer>
      </bs.Modal>
    </>
  );
}
