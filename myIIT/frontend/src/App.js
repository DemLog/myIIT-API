import React, {useState, useEffect} from 'react';
import bridge from '@vkontakte/vk-bridge';
import {
    Epic,
    Panel,
    Root, ScreenSpinner,
    Tabbar,
    TabbarItem,
    View,
} from '@vkontakte/vkui';
import '@vkontakte/vkui/dist/vkui.css';
import {
    Icon28EducationOutline,
    Icon28MessageAddBadgeOutline,
    Icon28Newsfeed,
    Icon28NotebookCheckOutline
} from "@vkontakte/icons";

import Auth from "./Auth/Auth.js";
import SideBar from "./SideBar/sidebar.js"
import News from "./News/News";
import Events from "./Events/Events";
import Timetable from "./Timetable/Timetable";
import Feedback from "./Feedback/Feedback";
import Settings from "./panels/settings.js"
import {useSwipeable} from "react-swipeable";
import AuthService from "./API/AuthService";

const App = () => {
    const [activeView, setActiveView] = useState('auth')
    const [activePanel, setActivePanel] = useState('main')
    const onPanelChange = (e) => {
        setActivePanel(e.currentTarget.dataset.to);
        setActiveSideBar(false);
    }

    const [fetchedUser, setUser] = useState(null);
    const [sessionUser, setSessionUser] = useState([]);

    const [activeStory, setActiveStory] = useState('news')
    const onStoryChange = (e) => setActiveStory(e.currentTarget.dataset.story);

    const [activateSideBar, setActiveSideBar] = useState(false)
    const onSideBarChange = () => setActiveSideBar(!activateSideBar)
    const handlerSwipe = useSwipeable({
        onSwiped: (SwipeEventData) => {
            if (SwipeEventData.dir == "Right" && !activateSideBar) setActiveSideBar(true);
            else if (SwipeEventData.dir == "Left" && activateSideBar) setActiveSideBar(false);
        }
    })

    const [popout, setPopout] = useState(<ScreenSpinner size='large'/>);

    const vkURL = window.location.search;
    const authService = new AuthService(vkURL);

    useEffect(() => {
        bridge.subscribe(({detail: {type, data}}) => {
            if (type === 'VKWebAppUpdateConfig') {
                const schemeAttribute = document.createAttribute('scheme');
                schemeAttribute.value = data.scheme ? data.scheme : 'client_light';
                document.body.attributes.setNamedItem(schemeAttribute);
            }
        });
    }, []);

    const goView = e => {
        if (typeof e != 'string')
            setActiveView(e.currentTarget.dataset.to);
        setActiveView(e);
    };

    return (
        <Root activeView={activeView}>
            <Auth id='auth' goView={goView} url={vkURL} api={authService} popout={popout} setPopout={setPopout}
                  vkUser={fetchedUser} setVKUser={setUser}/>
            <View id='main' activePanel={activePanel}>
                <Panel id='main'>
                    <div {...handlerSwipe}>
                        <SideBar activateSideBar={activateSideBar} closeSideBar={onSideBarChange} go={onPanelChange}
                                 vkUser={fetchedUser}/>
                        <Epic activeStory={activeStory} tabbar={
                            <Tabbar>

                                <TabbarItem
                                    onClick={onStoryChange}
                                    selected={activeStory === 'news'}
                                    data-story="news"
                                    text="Новости"
                                ><Icon28Newsfeed/>
                                </TabbarItem>

                                <TabbarItem
                                    onClick={onStoryChange}
                                    selected={activeStory === 'events'}
                                    data-story="events"
                                    text="Мероприятия"
                                ><Icon28NotebookCheckOutline/>
                                </TabbarItem>

                                <TabbarItem
                                    onClick={onStoryChange}
                                    selected={activeStory === 'timetable'}
                                    data-story="timetable"
                                    text="Расписание"
                                ><Icon28EducationOutline/>
                                </TabbarItem>

                                <TabbarItem
                                    onClick={onStoryChange}
                                    selected={activeStory === 'feedback'}
                                    data-story="feedback"
                                    text="Обратная связь"
                                ><Icon28MessageAddBadgeOutline/>
                                </TabbarItem>

                            </Tabbar>
                        }>
                            <News id='news' onSidebar={onSideBarChange} url={vkURL}/>
                            <Events id='events' onSidebar={onSideBarChange}/>
                            <Timetable id='timetable' onSidebar={onSideBarChange}/>
                            <Feedback id='feedback' onSidebar={onSideBarChange}/>
                        </Epic>
                    </div>
                </Panel>
                <Settings id="settings" go={onPanelChange}/>
            </View>
        </Root>
    );
}

export default App;
