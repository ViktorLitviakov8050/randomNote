import { useState, useEffect, useRef } from 'react';
import * as Notifications from 'expo-notifications';

Notifications.setNotificationHandler({
    handleNotification: async () => ({
        shouldShowAlert: true,
        shouldPlaySound: true,
        shouldSetBadge: true,
    }),
});

export default function useNotificationNote(callback) {
    const [note, setNote] = useState({})
    const responseListener = useRef();

    useEffect(() => {
        responseListener.current = Notifications.addNotificationResponseReceivedListener(response => {
            const note = response.notification.request.content.data;
            setNote(note)
            callback(note)
        });

        return () => {
            Notifications.removeNotificationSubscription(responseListener.current);
        };
    }, []);

    return { note };
}
