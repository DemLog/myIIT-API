import React, {useState, useEffect} from 'react';
import bridge from '@vkontakte/vk-bridge';
import {
    AdaptivityProvider, AppRoot,
    ConfigProvider,
    Root,
    ScreenSpinner,
} from '@vkontakte/vkui';
import '@vkontakte/vkui/dist/vkui.css';

import Auth from "./Auth/Auth";
import AuthService from "./API/AuthService";
import Main from "./Main";

const App = () => {
    const [activeView, setActiveView] = useState('auth');

    const [fetchedUser, setUser] = useState(null);

    const [popout, setPopout] = useState(<ScreenSpinner size='large'/>);

    const [schemeUser, setSchemeUser] = useState({
        scheme: 'bright_light',
        platform: 'ios'
    });
    const changeScheme = (e) => { // ГОВНОКОД
        const govno = schemeUser
        if (e.target.type === "checkbox" && e.target.name !== 'platform'){
            setSchemeUser(prevState => ({
                ...prevState,
                scheme: e.target.checked ? 'space_gray' : 'bright_light'
            })
            );
            govno.scheme = e.target.checked ? 'space_gray' : 'bright_light'
        }
        else {
            setSchemeUser(prevState => ({
                    ...prevState,
                    platform: e.target.value
                })
            );
            govno.platform = e.target.value;
        }
        bridge.send("VKWebAppStorageSet", {"key": "schemeUser", "value": JSON.stringify(govno)});
    };

    const vkURL = window.location.search;
    const authService = new AuthService(vkURL);
    const getToken = authService.getAutoTokenVKStorage.bind(authService);

    useEffect(() => {
        /*bridge.subscribe(({detail: {type, data}}) => {
            if (type === 'VKWebAppUpdateConfig') {
                const schemeAttribute = document.createAttribute('scheme');
                schemeAttribute.value = data.scheme ? data.scheme : 'client_light';
                document.body.attributes.setNamedItem(schemeAttribute);
            }
        });*/
        async function getScheme() {
            const response = await bridge.send("VKWebAppStorageGet", {"keys": ["schemeUser"]})
            if (response.keys[0]['value'] === "") return null;
            const data = JSON.parse(response.keys[0]['value']);
            if (data === "") return null;

            setSchemeUser(data);
        }

        getScheme();
    }, []);

    const goView = e => {
        if (typeof e != 'string')
            setActiveView(e.currentTarget.dataset.to);
        setActiveView(e);
    };

    return (
        <ConfigProvider platform={schemeUser.platform} scheme={schemeUser.scheme}>
            <AdaptivityProvider>
                <AppRoot>
                <Root activeView={activeView}>
                    <Auth id='auth' goView={goView} url={vkURL} api={authService} popout={popout}
                          setPopout={setPopout}
                          vkUser={fetchedUser} setVKUser={setUser}/>
                    <Main id='main' goView={goView} popout={popout} setPopout={setPopout} vkUser={fetchedUser}
                          token={getToken} setScheme={changeScheme} scheme={schemeUser}/>
                </Root>
                </AppRoot>
            </AdaptivityProvider>
        </ConfigProvider>
    );
}

export default App;
