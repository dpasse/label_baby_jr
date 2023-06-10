import React, { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import { HomePage } from './home/HomePage';

import './scss/styles.scss';

const element = document.getElementById('app') as HTMLElement;
const root = createRoot(element);

root.render(
  <StrictMode>
    <Router>
      <Routes>
        <Route index={true} element={<HomePage />} />
      </Routes>
    </Router>
  </StrictMode>
);