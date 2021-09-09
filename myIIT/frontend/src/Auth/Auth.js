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
import AuthService from '../API/AuthService'

const authService = new AuthService();

class Auth extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            snackbar: null,
            email: '',
            password: '',
        };

        this.messageErrorAuth = this.messageErrorAuth.bind(this);
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    componentDidMount() {
        const test = authService.loginUserVK(this.props.url);
        console.log(test.token);
    }

    messageErrorAuth() {
        /*if (this.state.snackbar) return;*/
        this.setState({
            snackbar:
                <Snackbar
                    onClose={() => this.setState({snackbar: null})}
                    before={<Avatar size={28}
                                    style={{background: 'var(--accent)'}}><Icon28CancelCircleFillRed/></Avatar>}
                >
                    Неверно указан E-mail или пароль
                </Snackbar>
        });
    }

    handleChange(e) {
        this.setState({
            [e.target.name]: e.target.value
        });
    }

    handleSubmit(e) {
        e.preventDefault()
        console.log(window.location.search);
        if (!this.state.email || !this.state.password) return this.messageErrorAuth()
    }

    render() {
        return (
            <View activePanel='main'>
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
                                        value={this.state.email}
                                        onChange={this.handleChange}
                                    />
                                </FormItem>

                                <FormItem top="Пароль">
                                    <Input
                                        type="password"
                                        name="password"
                                        placeholder="Введите пароль"
                                        value={this.state.password}
                                        onChange={this.handleChange}
                                    />
                                </FormItem>

                                <FormItem>
                                    <Button size="l" stretched onClick={this.handleSubmit}>Войти</Button>
                                </FormItem>
                            </FormLayout>
                        </div>
                    </Group>
                    {this.state.snackbar}
                </Panel>
            </View>
        )
    }

}

export default Auth;