import { View, StyleSheet } from 'react-native'
import React, { useEffect, useState } from 'react'
import Button from '../components/Button'
import Note from '../components/Note'
import useNotificationNote from '../components/useNotificationNote';
import { API_URL } from "@env"

const getRandomNote = async (callback) => {
    try {
        const response = await fetch(
            `${API_URL}/notes/getrandomnote`,
        );
        const json = await response.json();
        callback(json);
    } catch (error) {
        console.error(error);
    }
};

const MainScreen = () => {
    const [note, setNote] = useState({})

    useNotificationNote(setNote)

    useEffect(() => {
        getRandomNote((json) => {
            setNote(json);
        })
    }, []);

    const isNotePresent = JSON.stringify(note) !== '{}'

    return (
        <View style={styles.container}>
            {isNotePresent && <Note data={note} />}
            <View style={styles.buttons_container}>
                <Button color='green' title="Next" onPress={() => getRandomNote(setNote)} />
            </View>
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'space-between'
    },
    buttons_container: {
        flexDirection: 'row',
        paddingBottom: 10,
        width: '100%'
    },

})

export default MainScreen;
