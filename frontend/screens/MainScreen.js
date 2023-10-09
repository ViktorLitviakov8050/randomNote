import { View, StyleSheet } from 'react-native'
import React, { useEffect, useState } from 'react'
import Button from '../components/Button'
import Note from '../components/Note'


const getRandomNote = async (callback) => {
    try {
        const response = await fetch(
            'http://192.168.1.91:8000/notes/getrandomnote',
        );
        const json = await response.json();
        callback(json);
    } catch (error) {
        console.error(error);
    }
};



const MainScreen = ({note:note_from_notification}) => {
    const [note, setNote] = useState(note_from_notification)

    useEffect(() => {
        if (!note_from_notification)
            getRandomNote((json) => {
                setNote(json);
            })
    }, []);



    return (
        <View style={styles.container}>
            <Note data={note_from_notification} />
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

export default MainScreen


