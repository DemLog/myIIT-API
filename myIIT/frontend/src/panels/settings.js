import {
    ActionSheet, ActionSheetItem,
    Group,
    Header,
    Panel,
    PanelHeader,
    PanelHeaderBack,
    SimpleCell,
    Switch
} from "@vkontakte/vkui";


const settings = (props) => {
    const onScheme = props.scheme.scheme === 'space_gray';
    const selectPlatform = () => {
        props.setPopout(
            <ActionSheet
            onClose={() => props.setPopout(null)}
            iosCloseItem={<ActionSheetItem autoclose mode="cancel">Отменить</ActionSheetItem>}
        >
            <ActionSheetItem
                onChange={props.setScheme}
                checked={props.scheme.platform === 'ios'}
                name="platform"
                value="ios"
                autoclose
                selectable
            >
                iOS
            </ActionSheetItem>
                <ActionSheetItem
                    onChange={props.setScheme}
                    checked={props.scheme.platform === 'android'}
                    name="platform"
                    value="android"
                    autoclose
                    selectable
                >
                    Android
                </ActionSheetItem>
                <ActionSheetItem
                    onChange={props.setScheme}
                    checked={props.scheme.platform === 'vkcom'}
                    name="platform"
                    value="vkcom"
                    autoclose
                    selectable
                >
                    VKCom
                </ActionSheetItem>
        </ActionSheet>
    )};
    return (
        <Panel id={props.id}>
            <PanelHeader left={<PanelHeaderBack onClick={props.go} data-to="main"/>}>
                Настройки
            </PanelHeader>
            <Group>
                <Header mode="secondary">Внешний вид</Header>
                <SimpleCell disabled after={<Switch defaultChecked={onScheme} onChange={props.setScheme}/>}>Темная
                    тема</SimpleCell>
                <SimpleCell expandable onClick={selectPlatform} indicator={props.scheme.platform}>Тип оформления</SimpleCell>
            </Group>
        </Panel>
    );
}

export default settings;