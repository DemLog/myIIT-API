import axios from 'axios';

const API_URL = 'http://localhost:8000';

export default class CustomersService {

    constructor() {
    }

    loginUserMoodle(user) {
        const url = `${API_URL}api/v1/auth/login`;
        return axios.post(url, user).then(response => response.data)
    }

    loginUserVK(link) {
        const url = `${API_URL}/vk/${link}`;
        return axios.get(url).then(response => response.data);
    }
}