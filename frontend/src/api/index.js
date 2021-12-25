import Axios from "axios";

const axiosConfig = {
    baseURL: 'http://127.0.0.1:8000',
    timeout: 30000,
    withCredentials: true
};
const index = Axios.create(axiosConfig);

export default index
