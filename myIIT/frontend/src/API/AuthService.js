import axios from 'axios';
import bridge from "@vkontakte/vk-bridge";

const API_URL = 'https://192.168.1.49:8000/';

export default class AuthService {

    constructor(url) {
        this.vkURL = url;
    }

    static loginUserMoodle(user) {
        const url = `${API_URL}api/v1/auth/create/`;
        return axios.post(url,user).then(response => response.data)
    }

    loginUserVK(link = this.vkURL) {
        const url = `${API_URL}vk/${link}`;
        return axios.get(url).then(response => response.data).catch(() => null);
    }

    static getUserInfo(token) {
        const url = `${API_URL}api/v1/auth/user`;
        return axios.get(url, {
            headers: {
                'Authorization': `Token ${token}`
            }
        })
            .then(response => response.data)
            .catch(() => null);
    }

    setTokenVKStorage(userToken) {
        const data = Object.assign({}, userToken);
        data['lifetime'] = Date.now();
        return bridge.send("VKWebAppStorageSet", {"key": "userToken", "value": JSON.stringify(data)});
    }

    getAutoTokenVKStorage() {
        const setTokenVKStorage = this.setTokenVKStorage.bind(this);
        const loginUserVK = this.loginUserVK.bind(this);

        async function workingWithAsync() {
            const response = await bridge.send("VKWebAppStorageGet", {"keys": ["userToken"]})
            const data = JSON.parse(response.keys[0]['value']);
            if (data === "") return null;

            const lifeTime = data.lifetime;
            const nowTime = Date.now();
            if (nowTime - lifeTime >= 3600000) {
                const newToken = await loginUserVK();
                if (!newToken) return null;
                newToken['lifetime'] = Date.now();
                await setTokenVKStorage(newToken);
                return newToken;
            }
            return data;
        }

        return workingWithAsync();

    }
}