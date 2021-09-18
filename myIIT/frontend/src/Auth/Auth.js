import React, {useState, useEffect} from 'react';

import {
    Avatar,
    Button,
    FormItem,
    FormLayout,
    Group,
    Input,
    Panel,
    Snackbar, View
} from '@vkontakte/vkui';
import '@vkontakte/vkui/dist/vkui.css';
import {Icon28CancelCircleFillRed} from '@vkontakte/icons';

import logo from './img/logo.png';
import './style/Auth.css';
import bridge from "@vkontakte/vk-bridge";

const Auth = (props) => {

    const [snackbar, setSnackbar] = useState(null);
    const [inputData, changeInputData] = useState({
        'email': '',
        'password': ''
    });

    useEffect(() => {
        async function getStorageToken() {
            const fetchedUser = await bridge.send('VKWebAppGetUserInfo');
            props.setVKUser(fetchedUser);
            const tokenStorageVK = await props.api.getAutoTokenVKStorage();
            if (!tokenStorageVK) {
                const newToken = await props.api.loginUserVK();
                if (!newToken) return props.setPopout(null);
                await props.api.setTokenVKStorage(newToken);
            }
            props.setPopout(null);
            return props.goView('main');
        }

        getStorageToken();
    }, []);

    const messageError = (msg) => {
        setSnackbar(
            <Snackbar
                onClose={() => setSnackbar(null)}
                before={<Avatar size={28}
                                style={{background: 'var(--accent)'}}><Icon28CancelCircleFillRed/></Avatar>}
            >
                {msg}
            </Snackbar>
        )
    }

    const handleChange = (e) => {
        const {name, value} = e.target;
        changeInputData(prevState => ({
            ...prevState,
            [name]: value
        }));
    }

    const handleSubmit = (e) => {
        e.preventDefault()
        if (!inputData.email || !inputData.password) return messageError("Заполните все поля!");
        const query = {
            'user_id': props.vkUser.id,
            'email': inputData.email,
            'password': inputData.password
        };
        props.api.loginUserMoodle(query)
            .then((response) => {
                const addToken = {
                    user_id: response.user_id,
                    token: response.token
                };
                props.api.setTokenVKStorage(addToken);
                props.goView('main');
        })
            .catch(() => {
                return messageError('Неправильный E-Mail или пароль.')
        });
    }

    return (
        <View activePanel='main' popout={props.popout}>
            <Panel id='main'>
                {/*<PanelHeader>Авторизация</PanelHeader>*/}
                <Group>
                    <div className="auth-body">
                        <img className="logo" src={logo} alt="Логотип"/>
                        <FormLayout>
                            <FormItem top="E-mail Moodle">
                                <Input
                                    type="email"
                                    name="email"
                                    value={inputData.email}
                                    onChange={handleChange}
                                />
                            </FormItem>

                            <FormItem top="Пароль">
                                <Input
                                    type="password"
                                    name="password"
                                    placeholder="Введите пароль"
                                    value={inputData.password}
                                    onChange={handleChange}
                                />
                            </FormItem>

                            <FormItem>
                                <Button size="l" stretched onClick={handleSubmit}>Войти</Button>
                            </FormItem>
                        </FormLayout>
                    </div>
                </Group>
                {snackbar}
            </Panel>
        </View>
    )

}

export default Auth;