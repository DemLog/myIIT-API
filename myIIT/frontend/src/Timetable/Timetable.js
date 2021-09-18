import React from 'react';
import {
    Group,
    Panel,
    Placeholder,
    View
} from '@vkontakte/vkui';

import '@vkontakte/vkui/dist/vkui.css';

import HeaderMain from '../header.js'
import { Icon56GhostOutline } from '@vkontakte/icons';

const Timetable = (props) => {
    return (
        <View id={props.id} activePanel='main'>
            <Panel id='main'>
                <HeaderMain title='Расписание' openSidebar={props.onSidebar}/>
                <Group style={{height: '100px'}}>
                    <Placeholder icon={<Icon56GhostOutline width={56} height={56}/>}/>
                </Group>
            </Panel>
        </View>
    )
}

export default Timetable;