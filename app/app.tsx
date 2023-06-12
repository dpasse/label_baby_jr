import React, { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import { WorkspacePage } from './components/workspace';

import './scss/styles.scss';

const element = document.getElementById('app') as HTMLElement;
const root = createRoot(element);

root.render(
  <StrictMode>
    <Router>
      <Routes>
        <Route index={true} element={<WorkspacePage />} />
      </Routes>
    </Router>
  </StrictMode>
);