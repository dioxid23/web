import axios from "./index";

const baseAuthURL = '/projects'

const getData = response => response.data

export function getProjects() {
    return axios.get(`${baseAuthURL}`)
        .then(getData)
}
