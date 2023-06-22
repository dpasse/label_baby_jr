import _ from 'lodash';
import React, { useEffect, useState } from 'react';
import * as bs from 'react-bootstrap';

import { ICreateProjectArgs, IProject } from '../../common/types';
import { WorkspaceService } from '../../services';
import { CreateProjectModal } from './CreateProjectModal';
import { ProjectList } from './ProjectList';
import { Loading } from '../common';

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
            setProjects(projects.filter((project: IProject) => project.id !== identifier));
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

    return (
        <bs.Container>
            <bs.Row className="m-3 mb-5">
                <bs.Col md={{ span: 6, offset: 3 }}>
                    <CreateProjectModal handleSubmit={handleCreateNewProjectOnClickEvent} />
                </bs.Col>
            </bs.Row>
            <bs.Row md={4}>
                {
                    loading
                        ? <Loading />
                        : <ProjectList projects={projects} handleProjectDeleteOnClick={handleDeleteProjectOnClickEvent} />
                }
            </bs.Row>
        </bs.Container>
    );
}
