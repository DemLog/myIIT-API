import {
    Avatar,
    Group,
    Header,
    InfoRow,
    Panel,
    PanelHeader,
    PanelHeaderBack,
    ScreenSpinner,
    SimpleCell,
} from "@vkontakte/vkui";
import bridge from "@vkontakte/vk-bridge";
import {useEffect, useState} from "react";

const profile = (props) => {
    const [vkProfile, setVKProfile] = useState({
        first_name: 'Неизвестно',
        last_name: 'Неизвестно',
        photo_100: null,
        domain: 'id0'
    })
    useEffect(() => {
        async function getVKProfile() {
            const vkToken = await bridge.send("VKWebAppGetAuthToken", {"app_id": 7929802, "scope": ""});
            const vkProfile = await bridge.send("VKWebAppCallAPIMethod", {
                "method": "users.get",
                "request_id": "getVKProfile",
                "params": {
                    "user_ids": props.userInfo.user_id,
                    "fields": "photo_100, domain",
                    "v": "5.131",
                    "access_token": vkToken.access_token}
            });
            setVKProfile(vkProfile.response[0]);
            props.setPopout(null);
        }
        props.setPopout(<ScreenSpinner size='large'/>);
        getVKProfile();
    }, []);
    const urlVK = `https://vk.com/${vkProfile.domain}`

    return (
        <Panel id={props.id}>
            <PanelHeader left={<PanelHeaderBack onClick={props.go} data-to="main"/>}>
                Профил
            </PanelHeader>
            <Group>
                <Header mode="secondary">Привязанный профиль</Header>
                <SimpleCell
                    description={vkProfile.domain}
                    before={<Avatar src={vkProfile.photo_100}/>}
                    onClick={() => open(urlVK)}
                >
                    {vkProfile.first_name} {vkProfile.last_name}
                </SimpleCell>
            </Group>
            <Group>
                <Header mode="secondary">Информация о студенте</Header>
                <SimpleCell multiline>
                    <InfoRow header="Имя">
                        {props.userInfo.last_name} {props.userInfo.first_name} {props.userInfo.patronymic}
                    </InfoRow>
                </SimpleCell>
                <SimpleCell>
                    <InfoRow header="E-Mail">
                        {props.userInfo.email ? props.userInfo.email : "Неизвестно"}
                    </InfoRow>
                </SimpleCell>
                <SimpleCell>
                    <InfoRow header="Страна">
                        {props.userInfo.country ? props.userInfo.country : "Неизвестно"}
                    </InfoRow>
                </SimpleCell>
                <SimpleCell>
                    <InfoRow header="Город">
                        {props.userInfo.city ? props.userInfo.city : "Неизвестно"}
                    </InfoRow>
                </SimpleCell>
                <SimpleCell>
                    <InfoRow header="Статус">
                        {props.userInfo.status ? props.userInfo.status : "Неизвестно"}
                    </InfoRow>
                </SimpleCell>
                <SimpleCell>
                    <InfoRow header="Учебная группа">
                        {props.userInfo.study_group ? props.userInfo.study_group : "Неизвестно"}
                    </InfoRow>
                </SimpleCell>
                <SimpleCell>
                    <InfoRow header="Направление обучения">
                        {props.userInfo.direction ? props.userInfo.direction : "Неизвестно"}
                    </InfoRow>
                </SimpleCell>
                <SimpleCell>
                    <InfoRow header="Профиль">
                        {props.userInfo.profile ? props.userInfo.profile : "Неизвестно"}
                    </InfoRow>
                </SimpleCell>
                <SimpleCell>
                    <InfoRow header="Форма обучения">
                        {props.userInfo.form_study ? props.userInfo.form_study : "Неизвестно"}
                    </InfoRow>
                </SimpleCell>
            </Group>
        </Panel>
    );
}

export default profile;