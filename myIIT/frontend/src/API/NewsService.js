import axios from 'axios';
import bridge from "@vkontakte/vk-bridge";

const API_URL = 'https://myiit.demlovesky.ru/api/v1/news/';

export default class NewsService {

    constructor(token, vkToken) {
        this.token = token;
        this.vkToken = vkToken;
    }

    getCategoriesArticle() {
        return axios.get(API_URL+'category', {
            headers: {
                'Authorization': `Token ${this.token}`
            }
        })
            .then(response => response.data)
            .catch(() => null);
    }

    getArticles() {
        return axios.get(API_URL, {
            headers: {
                'Authorization': `Token ${this.token}`
            }
        })
            .then(response => response.data)
            .catch(() => null);
    }

}