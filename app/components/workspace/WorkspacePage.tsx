import React, { useEffect, useState } from 'react';
import { IProject } from '../../common/types';
import { WorkspaceService } from '../../services'

import * as bs from 'react-bootstrap';

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

  const cards = projects.map((row) => {
    return (
      <bs.Col key={ row.id }>
        <bs.Card className="p-3 m-3">
          <bs.Card.Body>
            <bs.Card.Title>{ row.name }</bs.Card.Title>
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
    </bs.Container>
  );
}
