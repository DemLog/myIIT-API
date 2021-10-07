import React, {Fragment, useEffect, useState} from 'react';
import {
    Avatar,
    Button, Card,
    CardGrid, Cell,
    ContentCard, Counter, Gallery,
    Group, HorizontalScroll,
    Panel, Placeholder, PullToRefresh, ScreenSpinner, Spacing,
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
    const [newsVK, setNewsVK] = useState({name: "", photo: "", posts: [], count: 20});

    const getNews = async function () {
        const userInfo = await props.token;
        const newsService = new NewsService(userInfo.token);

        const categoriesList = await newsService.getCategoriesArticle();
        setCategories(categoriesList);

        const articlesList = await newsService.getArticles();
        setNews(articlesList);
        props.setPopout(null);
    }

    useEffect(() => {
        const countVK = newsVK.count ? newsVK.count : 20;
        console.log(countVK)
        props.setPopout(<ScreenSpinner size='large'/>);
        if (tabsNews.activeTab === 'timeline') getNews();
        if (tabsNews.activeTab === 'iit') getNewsGroup(countVK);
        setFetching(prevState => ({enable: false, count: prevState.count}));
    }, [fetching.count, tabsNews, newsVK.count]);

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

    const onRefresh = () => setFetching(prevState => ({enable: true, count: prevState.count + 1}));

    const getNewsGroup = async (count) => {
        const vkToken = await bridge.send("VKWebAppGetAuthToken", {"app_id": 7929802, "scope": ""});
        const offsetVK = count > 100 ? count : 1;
        const countVK = count > 100 ? 20 : count;
        try {
            const vkNewsInfo = await bridge.send("VKWebAppCallAPIMethod", {
                "method": "groups.getById",
                "request_id": "getNewsInfo",
                "params": {
                    "group_id": 'csu_iit',
                    "v": "5.131",
                    "access_token": vkToken.access_token
                }
            });
            const vkNews = await bridge.send("VKWebAppCallAPIMethod", {
                "method": "wall.get",
                "request_id": "getNewsGroup",
                "params": {
                    "domain": 'csu_iit',
                    "count": countVK,
                    "offset": offsetVK,
                    "v": "5.131",
                    "access_token": vkToken.access_token
                }
            });
            setNewsVK(prevState => ({
                name: vkNewsInfo.response[0].name,
                photo_50: vkNewsInfo.response[0].photo_50,
                posts: count > 100 ? prevState.posts.concat(vkNews.response.items) : vkNews.response.items,
                count: prevState.count
            }));
            props.setPopout(null);
        } catch (e) {
            setNewsVK({posts: []});
            props.setPopout(null);
        }
    };

    const displayNewsGroup = () => {
        if (newsVK.posts.length === 0) return (
            <Placeholder
                header="ИИТ ЧелГУ"
                action={<Button size="m" onClick={() => open('https://vk.com/csu_iit')}>Присоединиться</Button>}
            >
                Невозможно получить последние новости, потому что Вы не подписаны на паблик
            </Placeholder>
        )

        const elements = [];
        newsVK.posts.forEach((article) => {
            if (article.copy_history) return;
            const photo = [];
            if (article.attachments) {
                article.attachments.forEach(a => {
                    if (!(a.type === "photo")) return;
                    photo.push(
                        <img src={a.photo.sizes[3].url} width={a.photo.sizes[3].width} height={a.photo.sizes[3].height}
                             style={{display: "block", margin: "0 auto"}}
                             className="VKPhoto"
                        />
                    )
                })
            }
            const datePub = new Date(article.date * 1000).toLocaleString('ru');
            elements.push(
                <Card>
                    <Cell before={<Avatar src={newsVK.photo_50}/>} description={datePub}>{newsVK.name}</Cell>
                    <div style={{margin: '3%', whiteSpace: "pre-wrap"}}>{article.text}</div>
                    {photo.length > 1 &&
                    <Gallery slideWidth="100%" style={{height: "auto"}} bullets="dark">{photo}</Gallery>}
                    {photo.length == 1 && photo[0]}
                </Card>
            )
        });
        return (
            <Fragment>
                <CardGrid size="l" mode="shadow">
                    {elements}
                </CardGrid>
                <div style={{marginTop: "10px"}}>
                    <Button
                        mode="secondary" style={{display: "block", margin: "0 auto"}} size="l"
                        onClick={() => setNewsVK(prevState => ({...prevState, count: prevState.count + 20}))}
                    >
                        Загрузить еще
                    </Button>
                </div>
            </Fragment>
        );
    }

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
                        {tabsNews.activeTab === 'iit' && displayNewsGroup()}
                    </Group>
                </PullToRefresh>
            </Panel>
        </View>
    )
}

export default News;