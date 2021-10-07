import {
    Epic,
    Panel,
    Tabbar,
    TabbarItem,
    View
} from "@vkontakte/vkui";
import {
    Icon28EducationOutline,
    Icon28MessageAddBadgeOutline,
    Icon28Newsfeed,
    Icon28NotebookCheckOutline
} from "@vkontakte/icons";

import SideBar from "./SideBar/sidebar";
import News from "./News/News";
import Events from "./Events/Events";
import Timetable from "./Timetable/Timetable";
import Feedback from "./Feedback/Feedback";

import Settings from "./panels/settings";
import Profile from "./panels/profile"

import {useEffect, useState} from "react";
import {useSwipeable} from "react-swipeable";

import AuthService from "./API/AuthService"
import bridge from "@vkontakte/vk-bridge";

const Main = (props) => {

    const [activePanel, setActivePanel] = useState('main')
    const onPanelChange = (e) => {
        setActivePanel(e.currentTarget.dataset.to);
        setActiveSideBar(false);
    }

    const [activeStory, setActiveStory] = useState('news')
    const onStoryChange = (e) => setActiveStory(e.currentTarget.dataset.story);

    const [activateSideBar, setActiveSideBar] = useState(false)
    const onSideBarChange = () => setActiveSideBar(!activateSideBar)
    const handlerSwipe = useSwipeable({
        onSwiped: (SwipeEventData) => {
            if (SwipeEventData.dir === "Right" && !activateSideBar) setActiveSideBar(true);
            else if (SwipeEventData.dir === "Left" && activateSideBar) setActiveSideBar(false);
        }
    })

    const [userInfo, setUserInfo] = useState({
        first_name: 'Error',
        last_name: 'Error',
        study_group: 'Error'
    });

    const test = () => {
        console.log(props.test)
    }

    useEffect(() => {
        async function getUserInfo() {
            const tokenObj = await props.token();
            const userInfo = await AuthService.getUserInfo(tokenObj.token);
            if (userInfo === null) {
                bridge.send("VKWebAppStorageSet", {"key": "userToken", "value": ""});
                return props.goView('auth');
            }
            setUserInfo(userInfo);
        };
        getUserInfo();
    }, []);

    return (
        <View id={props.id} activePanel={activePanel} popout={props.popout}>
            <Panel id='main'>
                <div {...handlerSwipe}>
                    <SideBar activateSideBar={activateSideBar} closeSideBar={onSideBarChange} go={onPanelChange}
                             vkUser={props.vkUser} userInfo={userInfo}/>
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
                        <News id='news' onSidebar={onSideBarChange}/>
                        <Events id='events' onSidebar={onSideBarChange}/>
                        <Timetable id='timetable' onSidebar={onSideBarChange}/>
                        <Feedback id='feedback' onSidebar={onSideBarChange}/>
                    </Epic>
                </div>
            </Panel>
            <Settings id="settings" go={onPanelChange} setScheme={props.setScheme} scheme={props.scheme} setPopout={props.setPopout}/>
            <Profile id="profile" go={onPanelChange} userInfo={userInfo} vkUser={props.vkUser} setPopout={props.setPopout}/>
        </View>
    );
}

export default Main;