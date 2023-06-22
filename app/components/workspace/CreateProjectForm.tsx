import React from 'react';

import * as bs from 'react-bootstrap';
import { ICreateProjectArgs } from '../../common/types';

export interface ICreateProjectProps {
    project: ICreateProjectArgs;
    handleNameChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
}

export const DEFAULT_CREATE_PROJECT_VALUES: ICreateProjectArgs = {
  name: '',
}

export function CreateProjectForm({ project, handleNameChange }: ICreateProjectProps): JSX.Element {
  return (
    <div className="form-group">
        <bs.Form.Label htmlFor="project-name">Name:</bs.Form.Label>
        <bs.Form.Control id="project-name"
                         type="text"
                         onChange={handleNameChange}
                         value={project.name} />
    </div>
  );
}
