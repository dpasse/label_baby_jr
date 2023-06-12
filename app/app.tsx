import React, { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import { Header } from './components/common';
import { WorkspacePage } from './components/workspace';
import { ProjectPage } from './components/project';

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-icons/font/bootstrap-icons.min.css'

import './scss/styles.scss';

const element = document.getElementById('app') as HTMLElement;
const root = createRoot(element);

const ProjectsPage = () => {
  return (
      <Routes>
          <Route path=':projectId/*' element={ <ProjectPage /> } />
      </Routes>
  );
};

root.render(
  <StrictMode>
    <Router>
      <Header />
      <Routes>
        <Route index={true} element={<WorkspacePage />} />
        <Route path='/projects/*' element={ <ProjectsPage /> } />
      </Routes>
    </Router>
  </StrictMode>
);