import axios from 'axios';

console.log(process.env)

const config = {
  baseURL: 'http://127.0.0.1:5000/api/',
  headers: {
    'Content-type': 'application/json'
  },
};

export default axios.create(config);
