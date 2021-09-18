import {PanelHeader, PanelHeaderButton} from "@vkontakte/vkui";
import { Icon28Menu } from '@vkontakte/icons';

const header = (props) => {
    return (
        <PanelHeader left={ <PanelHeaderButton onClick={props.openSidebar}><Icon28Menu /></PanelHeaderButton>}>
            {props.title}
        </PanelHeader>
    );
}

export default header;