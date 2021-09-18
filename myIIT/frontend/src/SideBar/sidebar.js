import {
    Avatar, Cell,
    Gradient,
    Group,
    Header, List,
    SimpleCell, Spacing,
    Text,
    Title
} from "@vkontakte/vkui";
import {
    Icon28Favorite,
    Icon28GhostOutline,
    Icon28InfoOutline,
    Icon28MessageOutline,
    Icon28Notifications, Icon28QrCodeOutline, Icon28SettingsOutline,
    Icon28UserCircleOutline
} from '@vkontakte/icons';
import React from "react";

import './sidebar.css'
import {useSwipeable} from "react-swipeable";

const sidebar = (props) => {

    return (
        <nav className={props.activateSideBar ? "nav nav--open" : "nav"}>
            <div className="nav__links">
                <Group>
                     <List>
                        <Gradient style={{
                            display: 'flex',
                            flexDirection: 'column',
                            alignItems: 'center',
                            justifyContent: 'center',
                            textAlign: 'center',
                        }}>
                            <Avatar size={96} src={props.vkUser.photo_100}/>
                            <Title style={{marginBottom: 8, marginTop: 20}} level="2" weight="medium">Имя из мудл</Title>
                            <Text style={{marginBottom: 24, color: 'var(--text_secondary)'}}>Группа из мудл</Text>
                        </Gradient>
                        <Header mode="secondary">Меню</Header>
                        <SimpleCell expandable before={<Icon28UserCircleOutline/>}>Мой профиль</SimpleCell>
                        <SimpleCell expandable before={<Icon28Notifications/>}>Уведомления</SimpleCell>
                        <SimpleCell expandable before={<Icon28MessageOutline/>}>Сообщения</SimpleCell>
                        <SimpleCell expandable before={<Icon28InfoOutline/>}>Контакты</SimpleCell>
                        <SimpleCell expandable before={<Icon28GhostOutline/>}>Интерактив</SimpleCell>
                        <SimpleCell onClick={props.go} data-to="settings" expandable
                                    before={<Icon28SettingsOutline/>}>Настройки</SimpleCell>
                        <SimpleCell expandable before={<Icon28Favorite/>}>Администрирование</SimpleCell>
                        <Spacing/>
                        <Cell expandable before={<Icon28QrCodeOutline/>}>Сканировать QR-код</Cell>
                    </List>
                </Group>
            </div>
            <div className="nav__overlay" onClick={props.closeSideBar}/>
        </nav>
    );
}

export default sidebar;