import React, { useEffect, useState } from 'react';
import { IProject } from '../../common/types';
import { WorkspaceService } from '../../services'

const workspaceService = new WorkspaceService();

export function WorkspacePage(): JSX.Element {
  const [loading, setLoading] = useState<boolean>(false);
  const [projects, setProjects] = useState<IProject[]>([]);

  useEffect(() => {
    if (loading) {
        return;
    }

    setLoading(true);
    workspaceService.getAll().then((response) => {
      setProjects(response);

      setLoading(false);
    });
  }, []);

  const body = projects.map((row) => {
      return (
          <div key={row.id}>
            <p>{ row.name }</p>
          </div>
      );
  });

  return (
    <div className='container'>
      { body }
    </div>
  );
}
