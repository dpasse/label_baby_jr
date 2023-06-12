import axios from 'axios';

const config = {
  baseURL: process.env.API_ROOT,
  headers: {
    'Content-type': 'application/json'
  },
};

export default axios.create(config);
