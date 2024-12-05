import axios from 'axios';

// Create an instance of axios with the base URL
const api = axios.create({
  baseURL: "http://localhost:5173"
});

// Export the Axios instance
export default api;