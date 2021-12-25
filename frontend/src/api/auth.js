import axios from "./index";

const baseAuthURL = '/users'

export function login({username, password}) {
    const bodyFormData = new FormData();

    bodyFormData.append('username', username)
    bodyFormData.append('password', password)

    return axios.post(`${baseAuthURL}/auth/login`, bodyFormData)
}

export function getUserName() {
    return axios.get(`${baseAuthURL}/me`)
        .then(response => response.data.first_name)
}

export function register(userData) {
    return axios.post(`${baseAuthURL}/auth/register`, userData)
}


export function logout() {
    return axios.post(`${baseAuthURL}/auth/logout`)
}
