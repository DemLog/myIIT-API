import React, {useState, useEffect} from 'react';
import bridge from '@vkontakte/vk-bridge';
import {
    Root,
    ScreenSpinner,
} from '@vkontakte/vkui';
import '@vkontakte/vkui/dist/vkui.css';

import Auth from "./Auth/Auth";
import AuthService from "./API/AuthService";
import Main from "./Main";

const App = () => {
    const [activeView, setActiveView] = useState('auth')

    const [fetchedUser, setUser] = useState(null);

    const [popout, setPopout] = useState(<ScreenSpinner size='large'/>);

    const vkURL = window.location.search;
    const authService = new AuthService(vkURL);
    const getToken = authService.getAutoTokenVKStorage.bind(authService);

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
            <Main id='main' goView={goView} popout={popout} setPopout={setPopout} vkUser={fetchedUser} token={getToken}/>
        </Root>
    );
}

export default App;
