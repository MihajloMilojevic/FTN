import React from 'react';
import AppContextProvider from './context/contextProvider';
import { BrowserRouter, Navigate, Route, Routes, } from 'react-router-dom';
import * as ClientComponents from './components/client';
import * as AdminComponents from './components/admin';
import * as ClientPages from "./pages/client";
import * as AdminPages from "./pages/admin";
import Error404 from './pages/404';
import ErrorPage from './pages/error';

import "./styles/global.css";
import { ScrollToTopRouter } from './components/common';

function App() {
    return (
        <BrowserRouter>
            <AppContextProvider>
                <ScrollToTopRouter />
                <Routes >
                    <Route path='/admin' element={<AdminComponents.Layout />}>
                        <Route path="/admin"  element={<Navigate replace to="/admin/organizers"/>} />
                        <Route path="/admin/organizers" element={<AdminPages.OrganizersPage />} />
                        <Route path="/admin/organizers/:organizerId/festivals" element={<AdminPages.OrganizersFestivalsPage />} />
                        <Route path="/admin/users" element={<AdminPages.UsersPage />} />
                        <Route path="/admin/error" element={<ErrorPage url="/admin" />} />
                        <Route path="/admin/*" element={<Error404 url="/admin" />} />
                    </Route>
                    <Route path='/' element={<ClientComponents.Layout />}>
                        <Route path="/" element={<ClientPages.Homepage />} />
                        <Route path="/organizers/:organizerId" element={<ClientPages.OrganizerPage />} />
                        <Route path="/organizers/:organizerId/festivals/:festivalId" element={<ClientPages.FestivalPage />} />
                        <Route path="/error" element={<ErrorPage url="/" />} />
                        <Route path="*" element={<Error404 url="/" />} />
                    </Route>
                </Routes>
            </AppContextProvider>
        </BrowserRouter>
    );
}

export default App;