import {Group, Panel, PanelHeader, PanelHeaderBack, SimpleCell} from "@vkontakte/vkui";
import {
    Icon28CheckShieldDeviceOutline,
    Icon28DevicesOutline,
    Icon28KeyOutline,
    Icon28MailOutline,
    Icon28PhoneOutline
} from '@vkontakte/icons';

const settings = (props) => {
    return (
        <Panel id={props.id}>
            <PanelHeader left={<PanelHeaderBack onClick={props.go} data-to="main"/>}>
                Настройки
            </PanelHeader>
            <Group>
                <Group mode="plain">
                    <SimpleCell indicator="+7 ••• •• •• 96" before={<Icon28PhoneOutline/>}>
                        Номер телефона
                    </SimpleCell>
                    <SimpleCell indicator="g•••@gmail.com" before={<Icon28MailOutline/>}>
                        Email
                    </SimpleCell>
                </Group>
                <Group mode="plain">
                    <SimpleCell indicator="Обновлён 3 года назад" before={<Icon28KeyOutline/>}>
                        Пароль
                    </SimpleCell>
                    <SimpleCell indicator="Вкл." before={<Icon28CheckShieldDeviceOutline/>}>
                        Подтверждение входа
                    </SimpleCell>
                    <SimpleCell indicator="2" before={<Icon28DevicesOutline/>}>
                        Привязанные устройства
                    </SimpleCell>
                </Group>
            </Group>
        </Panel>
    );
}

export default settings;