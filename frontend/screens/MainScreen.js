import { View, StyleSheet } from 'react-native'
import React, { useEffect, useState } from 'react'
import Button from '../components/Button'
import Note from '../components/Note'
import useNotificationNote from '../hooks/useNotificationNote';
import useAPI from '../hooks/useAPI';

const MainScreen = () => {
    const [note, setNote] = useState({})
    const { fetchData } = useAPI(`notes/getrandomnote`, setNote, console.log);

    useNotificationNote(setNote)

    useEffect(() => {
        fetchData();
    }, []);

    const isNotePresent = JSON.stringify(note) !== '{}'

    return (
        <View style={styles.container}>
            {isNotePresent && <Note data={note} />}
            <View style={styles.buttons_container}>
                <Button color='green' title="Next" onPress={fetchData} />
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
