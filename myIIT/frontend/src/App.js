import React, {useState, useEffect} from 'react';
import bridge from '@vkontakte/vk-bridge';
import {
    View,
    ScreenSpinner,
    AdaptivityProvider,
    AppRoot,
    Root,
} from '@vkontakte/vkui';
import '@vkontakte/vkui/dist/vkui.css';

import Auth from "./Auth/Auth.js";
import Main from "./Main.js"

const App = () => {
    const [activeView, setActiveView] = useState('main')
    const [fetchedUser, setUser] = useState(null);
    //const [popout, setPopout] = useState(<ScreenSpinner size='large' />);

    const vkURL = window.location.search;

    useEffect(() => {
        bridge.subscribe(({detail: {type, data}}) => {
            if (type === 'VKWebAppUpdateConfig') {
                const schemeAttribute = document.createAttribute('scheme');
                schemeAttribute.value = data.scheme ? data.scheme : 'client_light';
                document.body.attributes.setNamedItem(schemeAttribute);
            }
        });
        /*async function fetchData() {
            const user = await bridge.send('VKWebAppGetUserInfo');
            setUser(user);
            setPopout(null);
        }
        fetchData();*/
    }, []);

    const goView = e => {
        setActiveView(e.currentTarget.dataset.to);
    };

    return (
        <AdaptivityProvider>
            <AppRoot>
                <Root activeView={activeView}>
                    <Auth id='auth' goView={goView} url={vkURL}/>
                    <Main id='main' goView={goView}/>
                </Root>
            </AppRoot>
        </AdaptivityProvider>
    );
}

export default App;
