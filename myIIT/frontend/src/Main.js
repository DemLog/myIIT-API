import React from 'react';
import {
    Epic,
    Tabbar,
    TabbarItem,
    View
} from '@vkontakte/vkui';

import '@vkontakte/vkui/dist/vkui.css';
import {
    Icon28EducationOutline,
    Icon28MessageAddBadgeOutline,
    Icon28Newsfeed,
    Icon28NotebookCheckOutline,
} from '@vkontakte/icons';

class Main extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            activeStory: 'news',
        };

        this.handleChangeStory = this.handleChangeStory.bind(this)
    }


    handleChangeStory(e) {
        this.setState({
            activeStory: e.currentTarget.dataset.story
        });
    }

    render() {
        return (
            <View>
                <Epic activeStory={this.state.activeStory} tabbar={
                    <Tabbar>

                        <TabbarItem
                            onClick={this.handleChangeStory}
                            selected={this.state.activeStory === 'news'}
                            data-story="news"
                            text="Новости"
                        ><Icon28Newsfeed/>
                        </TabbarItem>

                        <TabbarItem
                            onClick={this.handleChangeStory}
                            selected={this.state.activeStory === 'events'}
                            data-story="events"
                            text="Мероприятия"
                        ><Icon28NotebookCheckOutline/>
                        </TabbarItem>

                        <TabbarItem
                            onClick={this.handleChangeStory}
                            selected={this.state.activeStory === 'timetable'}
                            data-story="timetable"
                            text="Расписание"
                        ><Icon28EducationOutline/>
                        </TabbarItem>

                        <TabbarItem
                            onClick={this.handleChangeStory}
                            selected={this.state.activeStory === 'feedback'}
                            data-story="feedback"
                            text="Обратная связь"
                        ><Icon28MessageAddBadgeOutline/>
                        </TabbarItem>

                    </Tabbar>
                }/>
            </View>
        )
    }
}

export default Main;