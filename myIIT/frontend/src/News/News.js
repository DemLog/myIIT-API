import React, {useEffect, useState} from 'react';
import {
    CardGrid,
    ContentCard, Counter,
    Group, HorizontalScroll,
    Panel, Placeholder, PullToRefresh, ScreenSpinner,
    Tabs,
    TabsItem,
    View
} from '@vkontakte/vkui';

import '@vkontakte/vkui/dist/vkui.css';

import HeaderMain from '../header.js'
import NewsService from "../API/NewsService";
import bridge from "@vkontakte/vk-bridge";
import {Icon56ArticleOutline, Icon56GhostOutline} from "@vkontakte/icons";

const News = (props) => {
    const [tabsNews, setTabsNews] = useState({
        activeTab: 'timeline',
        activeCategory: 'all'
    });

    const [fetching, setFetching] = useState({enable: false, count: 0});
    const [categories, setCategories] = useState([]);
    const [news, setNews] = useState([]);

    const getNews = async function () {
        const userInfo = await props.token;
        const newsService = new NewsService(userInfo.token);

        const categoriesList = await newsService.getCategoriesArticle();
        setCategories(categoriesList);

        const articlesList = await newsService.getArticles();
        setNews(articlesList);
    }

    useEffect(() => {
        props.setPopout(<ScreenSpinner size='large'/>);
        getNews();
        props.setPopout(null);
        setFetching(prevState => ({enable: false, count: prevState.count}));
    }, [fetching.count, tabsNews.activeCategory]);

    const displayCategories = () => {
        if (categories.length === 0) return undefined;
        const elements = [];
        categories.forEach((category) => {
            const count = news.filter(x => x.category === category.id && !x.is_published).length;
            elements.push(
                <TabsItem
                    onClick={() => setTabsNews(prevState => ({...prevState, activeCategory: category.slug}))}
                    selected={tabsNews.activeCategory === category.slug}
                    after={<Counter>{count}</Counter>}
                >
                    {category.name}
                </TabsItem>
            )
        });
        return (
            <Tabs mode="buttons">
                <HorizontalScroll>
                    <TabsItem
                        onClick={() => setTabsNews(prevState => ({...prevState, activeCategory: 'all'}))}
                        selected={tabsNews.activeCategory === 'all'}
                        after={<Counter>{news.length}</Counter>}
                    >
                        Все
                    </TabsItem>
                    {elements}
                </HorizontalScroll>
            </Tabs>
        );
    };

    const displayNews = () => {
        if (news.length === 0) return (
            <Placeholder
                icon={<Icon56ArticleOutline width={112} height={112}/>}
                style={{height: '50%'}}
            >
                Новостей нет:)
            </Placeholder>
        );
        const elements = [];
        news.forEach((article) => {
            if (!(tabsNews.activeCategory === 'all')) {
                const categoryID = categories.find(category => category.slug === tabsNews.activeCategory).id;
                if (!(categoryID === article.category)) return;
            }
            if (article.is_published) return;
            elements.push(
                <ContentCard
                    subtitle={"#" + categories[article.category - 1].name}
                    header={article.title}
                    text={article.text}
                />
            )
        });
        return (
            <CardGrid size="l">
                {elements}
            </CardGrid>
        );
    };

    const onRefresh = () => setFetching(prevState => ({enable: true, count: prevState.count+1}));

    const getNewsGroup = () => {

    };

    return (
        <View id={props.id} activePanel='main'>
            <Panel id='main'>
                <HeaderMain title='Новости' openSidebar={props.onSidebar}/>
                <Tabs>
                    <TabsItem
                        onClick={() => setTabsNews(prevState => ({...prevState, activeTab: 'timeline'}))}
                        selected={tabsNews.activeTab === 'timeline'}
                    >
                        Лента
                    </TabsItem>
                    <TabsItem
                        onClick={() => setTabsNews(prevState => ({...prevState, activeTab: 'iit'}))}
                        selected={tabsNews.activeTab === 'iit'}
                    >
                        ИИТ ЧелГУ
                    </TabsItem>
                </Tabs>
                {tabsNews.activeTab === 'timeline' && displayCategories()}
                <PullToRefresh onRefresh={onRefresh} isFetching={fetching.enable}>
                    <Group>
                        {tabsNews.activeTab === 'timeline' && displayNews()}
                    </Group>
                </PullToRefresh>
            </Panel>
        </View>
    )
}

export default News;