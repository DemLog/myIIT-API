import React from "react";
import ReactDOM from "react-dom";
import bridge from "@vkontakte/vk-bridge";
import App from "./App";
import {AdaptivityProvider, AppRoot, ConfigProvider} from "@vkontakte/vkui";

bridge.send("VKWebAppInit");

ReactDOM.render(
    <ConfigProvider>
        <AdaptivityProvider>
            <AppRoot>
                <App />
            </AppRoot>
        </AdaptivityProvider>
    </ConfigProvider>, document.getElementById("root"));
